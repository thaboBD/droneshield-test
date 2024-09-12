import pytest
import json
from playwright.sync_api import expect, APIRequestContext
from src.api.utils.pet_data_util import pet
from src.api.config import get_api_base_url

@pytest.mark.api
@pytest.mark.describe("Pet endpoint : POST Method")
class TestPetEndpointCreate:

    @pytest.fixture(autouse=True)
    def setup(self, api_request: APIRequestContext):
        self.base_url = get_api_base_url()
        self.endpoint = f"{self.base_url}/pet"

    @pytest.mark.it("should create a new pet")
    def test_create_new_pet(self, api_request: APIRequestContext):
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        response = api_request.post(self.endpoint, 
                                    headers=headers,
                                    data=json.dumps(pet))
        print(f"Full URL: {response.url}")  # Add this line

        assert response.ok, f"Expected OK response, got {response.status} {response.status_text}"
        response_body = response.json()
        assert response_body['id'] == pet['id'], f"Expected id {pet['id']}, got {response_body['id']}"
        assert response_body == pet, f"Response body doesn't match expected pet data"

    @pytest.mark.it("should not create a new pet as some required fields are missing")
    def test_create_pet_missing_fields(self, api_request: APIRequestContext):
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        response = api_request.post(self.endpoint, 
                                    headers=headers,
                                    data=json.dumps({'name': 'new pet'}))
        assert response.status == 200
        


    @pytest.mark.it("should not create a new pet as request body is empty")
    def test_create_pet_empty_body(self, api_request: APIRequestContext):
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        response = api_request.post(self.endpoint, 
                                    headers=headers,
                                    data=json.dumps({}))
        print(f"Full URL: {response.url}")  # Add this line

        assert response.status == 200
        