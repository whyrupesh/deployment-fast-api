from typing import Optional

from fastapi import FastAPI

from app.schemas import (
    MatchInvestorsRequest,
    MatchInvestorsResponse,
    MatchedInvestor,
    MatchedDomain
)

from app.services.matcher import match_investors

app = FastAPI()


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