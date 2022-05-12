async def test_example(example_app, base_url, jp_fetch):
    """Request the main page of ExampleApp"""
    response = await jp_fetch(base_url)
    assert response.code == 200