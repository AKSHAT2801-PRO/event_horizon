from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from controllers.station import handle_station

router = APIRouter()

@router.get("/recorded")
async def get_station(station_name: str = Query(...)):
    """
    Get recorded station data by station name
    """
    return await handle_station(station_name=station_name)
