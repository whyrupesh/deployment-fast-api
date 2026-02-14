from sentence_transformers import SentenceTransformer
from app.db import get_connection

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def match_investors(
    startup_description: str,
    top_domains: int,
    top_investors: int,
    min_similarity: float
):
    query_embedding = model.encode(startup_description).tolist()

    conn = get_connection()
    cur = conn.cursor()

    # 1️⃣ Find top domains
    cur.execute("""
        SELECT name, description,
               1 - (embedding <=> %s::vector) AS similarity
        FROM domains
        WHERE embedding IS NOT NULL
        ORDER BY embedding <=> %s::vector
        LIMIT %s;
    """, (query_embedding, query_embedding, top_domains))

    domain_rows = cur.fetchall()

    matched_domains = [
        {
            "domain": row["name"],
            "similarity": float(row["similarity"])
        }
        for row in domain_rows
        if row["similarity"] >= min_similarity
    ]

    domain_names = [d["domain"] for d in matched_domains]

    if not domain_names:
        return {"matched_domains": [], "matched_investors": []}

    # 2️⃣ Find investors
    cur.execute("""
        SELECT
            i.id::text AS investor_id,
            i.slug,
            i.name,
            ARRAY_AGG(DISTINCT d.name) AS matched_domains,
            COUNT(DISTINCT d.id) AS domain_match_count
        FROM investors i
        JOIN investor_domains idm ON idm.investor_id = i.id
        JOIN domains d ON d.id = idm.domain_id
        WHERE d.name = ANY(%s)
        GROUP BY i.id
        ORDER BY domain_match_count DESC
        LIMIT %s;
    """, (domain_names, top_investors))

    investors = cur.fetchall()

    cur.close()
    conn.close()

    return {
        "matched_domains": matched_domains,
        "matched_investors": investors
    }
