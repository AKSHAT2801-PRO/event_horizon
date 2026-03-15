from fastapi import APIRouter, Query
from controllers.trajectory import handle_meteor_data

router = APIRouter()

@router.get("/trajectory")
async def get_trajectory(event_id: str = Query(...)):
    """
    Get meteor trajectory data by event ID
    """
    return await handle_meteor_data(event_id=event_id)
