from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI

from app.schemas import (
    MatchInvestorsRequest,
    MatchInvestorsResponse,
    MatchedInvestor,
    MatchedDomain
)

from app.services.matcher import match_investors
from app.routers import investors
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.middleware("http")
async def log_requests(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    logger.info(
        f"Method: {request.method} Path: {request.url.path} "
        f"Status: {response.status_code} Time: {process_time:.2f}ms"
    )
    return response

app.include_router(investors.router)

# CORS configuration
origins = [
    "http://localhost:3000",
    "https://fundizr-frontend-v2-cvco.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello")
def hello():
    return {"message": "Hello from the /hello endpoint!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}



@app.post("/api/v1/match-investors", response_model=MatchInvestorsResponse)
def match_investors_endpoint(payload: MatchInvestorsRequest):
    result = match_investors(
        startup_description=payload.startup_description,
        top_domains=payload.top_domains,
        top_investors=payload.top_investors,
        min_similarity=payload.min_domain_similarity
    )

    return {
        "matched_domains": [
            MatchedDomain(**d) for d in result["matched_domains"]
        ],
        "matched_investors": [
            MatchedInvestor(**i) for i in result["matched_investors"]
        ]
    }