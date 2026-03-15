from database import get_trajectory_results_collection
from fastapi import HTTPException
from typing import Dict
from bson import ObjectId
import traceback

def serialize_doc(doc):
    """Convert MongoDB documents to JSON-serializable format"""
    if doc is None:
        return None
    if isinstance(doc, ObjectId):
        return str(doc)
    if isinstance(doc, dict):
        return {k: serialize_doc(v) for k, v in doc.items()}
    if isinstance(doc, list):
        return [serialize_doc(item) for item in doc]
    return doc

async def handle_meteor_data(event_id: str) -> Dict:
    """
    Get meteor trajectory data by event ID
    """
    try:
        collection = await get_trajectory_results_collection()
        trajectory = await collection.find_one({"event_id": event_id})
        
        if not trajectory:
            raise HTTPException(status_code=404, detail="Trajectory not found")
        
        start_point = trajectory.get("start_point", {})
        end_point = trajectory.get("end_point", {})
        
        data = {
            "startLat": start_point.get("latitude"),
            "startLng": start_point.get("longitude"),
            "startAltKm": start_point.get("altitude"),
            "endLat": end_point.get("latitude"),
            "endLng": end_point.get("longitude"),
            "endAltKm": end_point.get("altitude"),
            "mass": trajectory.get("mass"),
            "initial_velocity": trajectory.get("initial_velocity"),
        }
        
        return serialize_doc(data)
    
    except HTTPException:
        raise
    except Exception as err:
        print(f"Trajectory endpoint error: {str(err)}")
        print(traceback.format_exc())
        raise HTTPException(
            status_code=500,
            detail=f"Invalid Data: {str(err)}"
        )
