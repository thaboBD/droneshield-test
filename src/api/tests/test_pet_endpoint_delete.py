import pytest
from playwright.sync_api import APIRequestContext
from src.api.utils.pet_data_util import pet  
from src.api.config import get_api_base_url

base_url = get_api_base_url()

@pytest.fixture(scope="function")
def create_pet(api_request: APIRequestContext):
    response = api_request.post(f'{base_url}/pet', data=pet)
    assert response.status == 200, f"Failed to create pet. Status: {response.status}"

@pytest.mark.api
@pytest.mark.describe("Pet endpoint : DELETE Method")
class TestPetEndpointDelete:

    @pytest.fixture(autouse=True)
    def setup(self, api_request: APIRequestContext):
        self.base_url = get_api_base_url()
        self.endpoint = f"{self.base_url}/pet"

    @pytest.mark.it("should delete an existing pet")
    def test_delete_existing_pet(self, api_request: APIRequestContext, create_pet):
        response = api_request.delete(f"{self.endpoint}/{pet['id']}")
        assert response.status == 200, f"Expected status 200, got {response.status}"

    @pytest.mark.it("should return 404 for non-existing pet")
    def test_delete_non_existing_pet(self, api_request: APIRequestContext):
        response = api_request.delete(f"{self.endpoint}/{pet['id'] + 1}")
        assert response.status == 404, f"Expected status 404, got {response.status}"