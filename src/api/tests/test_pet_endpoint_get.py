import pytest
from playwright.sync_api import APIRequestContext
from src.api.utils.pet_data_util import pet
from src.api.types.pet_status_types import PetStatus
from src.api.config import get_api_base_url

@pytest.fixture(scope="module")
def pet_id():
    return pet['id']

@pytest.fixture(scope="function")
def create_pet(api_request: APIRequestContext):
    base_url = get_api_base_url()
    response = api_request.post(f'{base_url}/pet', data=pet)
    assert response.status == 200, f"Failed to create pet. Status: {response.status}"
    return pet['id']

@pytest.mark.api
@pytest.mark.describe("Pet endpoint : GET Method")
class TestPetEndpointGet:

    @pytest.fixture(autouse=True)
    def setup(self, api_request: APIRequestContext):
        self.base_url = get_api_base_url()
        self.endpoint = f"{self.base_url}/pet"

    @pytest.mark.it("should retrieve pet information by ID for existing pet")
    def test_get_existing_pet(self, api_request: APIRequestContext, create_pet):
        pet_id = create_pet
        response = api_request.get(f"{self.endpoint}/{pet_id}")
        assert response.status == 200, f"Expected status 200, got {response.status}"
        response_body = response.json()
        assert response_body, "Response body should not be empty"
        assert response_body['id'] == pet_id, f"Expected id {pet_id}, got {response_body['id']}"

    @pytest.mark.it("should return 404 for non-existing pet")
    def test_get_non_existing_pet(self, api_request: APIRequestContext, pet_id):
        response = api_request.get(f"{self.endpoint}/{pet_id + 1}")
        assert response.status == 404, f"Expected status 404, got {response.status}"

@pytest.mark.api
@pytest.mark.describe("Retrieve Pet Information by Status")
class TestRetrievePetByStatus:

    @pytest.fixture(autouse=True)
    def setup(self, api_request: APIRequestContext):
        self.base_url = get_api_base_url()
        self.endpoint = f"{self.base_url}/pet"

    @pytest.mark.it("should retrieve pet information by status")
    def test_get_pet_by_status(self, api_request: APIRequestContext):
        response = api_request.get(f"{self.endpoint}/findByStatus?status={PetStatus.AVAILABLE}")
        assert response.status == 200, f"Expected status 200, got {response.status}"
      
