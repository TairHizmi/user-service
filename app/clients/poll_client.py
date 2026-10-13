import httpx
from fastapi import HTTPException

from app.config import settings


class PollClient:
    def delete_user_answers(self, user_id: int) -> None:
        try:
            response = httpx.delete(
                f"{settings.poll_service_url}/answers/user/{user_id}", timeout=5
            )
            response.raise_for_status()
        except httpx.HTTPError:
            raise HTTPException(status_code=503, detail="Poll service is unavailable")
