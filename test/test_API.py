import sys
sys.path.append(".")

import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_events_endpoint_ok():
    payload = {"lsEvents": list(range(60))}  # sample input

    async with AsyncClient(app=app, base_url="http://test") as client:
        resp = await client.post("/events", json=payload)

    assert resp.status_code == 200
    body = resp.json()
    assert body is False  # adapt to your actual response schema
