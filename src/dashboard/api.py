"""
Security Intelligence Dashboard — FastAPI Backend
Exposes pipeline results via REST API for the SOC dashboard.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import json

app = FastAPI(
    title="Cyber Risk Intelligence Platform",
    description="Unified cybersecurity threat detection, risk scoring, and adaptive defense API.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="."), name="static")

RESULTS_PATH = Path("output/results.json")


def _load_results() -> dict:
    if not RESULTS_PATH.exists():
        raise HTTPException(status_code=503, detail="Pipeline results not yet available. Run the pipeline first.")
    with open(RESULTS_PATH) as f:
        return json.load(f)


from fastapi.responses import FileResponse

@app.get("/", tags=["Frontend"])
def serve_frontend():
    return FileResponse("index.html")


@app.get("/summary", tags=["Dashboard"])
def get_summary():
    """High-level pipeline run summary."""
    return _load_results().get("summary", {})


@app.get("/risk-scores", tags=["Risk"])
def get_risk_scores(min_score: float = 0.0, risk_level: str = None):
    """Get all entity risk scores. Filter by min_score or risk_level."""
    scores = _load_results().get("risk_scores", [])
    if min_score:
        scores = [s for s in scores if s["score"] >= min_score]
    if risk_level:
        scores = [s for s in scores if s["risk_level"] == risk_level.upper()]
    return scores


@app.get("/attack-chains", tags=["Threats"])
def get_attack_chains():
    """Get all correlated attack chains."""
    return _load_results().get("attack_chains", [])


@app.get("/privacy-alerts", tags=["Privacy"])
def get_privacy_alerts(severity: str = None):
    """Get privacy risk alerts. Filter by severity."""
    alerts = _load_results().get("privacy_alerts", [])
    if severity:
        alerts = [a for a in alerts if a["severity"] == severity.upper()]
    return alerts


@app.get("/recommendations", tags=["Defense"])
def get_recommendations(entity: str = None):
    """Get adaptive defense recommendations. Filter by entity."""
    recs = _load_results().get("recommendations", [])
    if entity:
        recs = [r for r in recs if r["entity"] == entity]
    return recs


@app.get("/entity/{entity_name}", tags=["Entity"])
def get_entity_profile(entity_name: str):
    """Full profile for a single entity: risk score + chains + recommendations."""
    data = _load_results()
    scores = [s for s in data.get("risk_scores", []) if s["entity"] == entity_name]
    chains = [c for c in data.get("attack_chains", []) if c["entity"] == entity_name]
    recs   = [r for r in data.get("recommendations", []) if r["entity"] == entity_name]
    alerts = [a for a in data.get("privacy_alerts", []) if a["entity"] == entity_name]

    if not scores:
        raise HTTPException(status_code=404, detail=f"Entity '{entity_name}' not found.")

    return {
        "entity":          entity_name,
        "risk_score":      scores[0] if scores else None,
        "attack_chains":   chains,
        "privacy_alerts":  alerts,
        "recommendations": recs,
    }

# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import FileResponse
# from pathlib import Path
# import json

# app = FastAPI(title="Cyber Risk Intelligence Platform", version="1.0.0")

# app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# app.mount("/static", StaticFiles(directory="static"), name="static")

# RESULTS_PATH = Path("output/results.json")

# def _load_results():
#     if not RESULTS_PATH.exists():
#         raise HTTPException(status_code=503, detail="Run the pipeline first.")
#     with open(RESULTS_PATH) as f:
#         return json.load(f)

# @app.get("/", response_class=FileResponse)
# def root():
#     return FileResponse("static/index.html")

# @app.get("/summary")
# def get_summary():
#     return _load_results().get("summary", {})

# @app.get("/risk-scores")
# def get_risk_scores():
#     return _load_results().get("risk_scores", [])

# @app.get("/privacy-alerts")
# def get_privacy_alerts():
#     return _load_results().get("privacy_alerts", [])

# @app.get("/attack-chains")
# def get_attack_chains():
#     return _load_results().get("attack_chains", [])

# @app.get("/recommendations")
# def get_recommendations():
#     return _load_results().get("recommendations", [])

# @app.get("/entity/{entity_name}")
# def get_entity(entity_name: str):
#     data = _load_results()
#     scores = [s for s in data.get("risk_scores", []) if s["entity"] == entity_name]
#     if not scores:
#         raise HTTPException(status_code=404, detail=f"Entity '{entity_name}' not found.")
#     return {
#         "entity": entity_name,
#         "risk_score": scores[0],
#         "attack_chains": [c for c in data.get("attack_chains", []) if c["entity"] == entity_name],
#         "privacy_alerts": [a for a in data.get("privacy_alerts", []) if a["entity"] == entity_name],
#         "recommendations": [r for r in data.get("recommendations", []) if r["entity"] == entity_name],
#     }
