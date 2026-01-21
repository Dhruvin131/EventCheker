import pytest
from httpx import AsyncClient
from app.main import app  # your FastAPI app

@pytest.mark.asyncio
async def test_high_volume_events():
    payload = {"lsEvents": list(range(200000))}  # 200,000 events
    async with AsyncClient(app=app, base_url="http://test") as client:
        resp = await client.post("/events", json=payload)
    assert resp.status_code == 200
    # 200,000 events spread out over 200,000 seconds -> should NOT exceed
    assert resp.json() is False

@pytest.mark.asyncio
async def test_exceeds_limit():
    payload = {"lsEvents": [i % 5 for i in range(101)]}  # 101 events within 60s
    async with AsyncClient(app=app, base_url="http://test") as client:
        resp = await client.post("/events", json=payload)
    assert resp.status_code == 200
    assert resp.json() is True

@pytest.mark.asyncio
async def test_does_not_exceed_limit():
    payload = {"lsEvents": list(range(100))}  # 100 events in 100s
    async with AsyncClient(app=app, base_url="http://test") as client:
        resp = await client.post("/events", json=payload)
    assert resp.status_code == 200
    assert resp.json() is False

@pytest.mark.asyncio
async def test_non_sorted_input():
    payload = {"lsEvents": [10, 5, 1, 2, 5, 8, 3, 4] * 5}  # 40 events total
    async with AsyncClient(app=app, base_url="http://test") as client:
        resp = await client.post("/events", json=payload)
    assert resp.status_code == 200
    assert resp.json() is False

@pytest.mark.asyncio
async def test_invalid_input():
    payload = {"lsEvents": ["a", "b", "c"]}  # Invalid input
    async with AsyncClient(app=app, base_url="http://test") as client:
        resp = await client.post("/events", json=payload)
    # FastAPI + Pydantic will automatically return 422 for invalid types
    assert resp.status_code == 422
