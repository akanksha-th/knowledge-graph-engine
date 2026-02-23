def test_analyze_route(client):
    response = client.post("/analyze")
    assert response.status_code == 200
    assert response.json() == {"message": "coming soon!"}