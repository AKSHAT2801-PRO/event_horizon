from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Event Schemas
class Radiant(BaseModel):
    ra: float
    dec: float

class Event(BaseModel):
    event_id: str
    datetime_utc: datetime
    shower_code: str
    station_count: int
    peak_magnitude: float
    approx_velocity: float
    region: str
    radiant: Radiant

class EventResponse(BaseModel):
    event_id: str
    datetime_utc: datetime
    shower_code: str
    station_count: int
    peak_magnitude: float
    approx_velocity: float
    region: str
    radiant: Radiant

# Station Schemas
class Location(BaseModel):
    latitude: float
    longitude: float
    altitude: float

class Station(BaseModel):
    station_name: str
    location: Location
    shower_code: str

class StationResponse(BaseModel):
    station_name: str
    latitude: float
    longitude: float
    altitude: float
    shower_code: str

# Trajectory Schemas
class Point(BaseModel):
    latitude: float
    longitude: float
    altitude: float

class TrajectoryResult(BaseModel):
    event_id: str
    start_point: Point
    end_point: Point
    mass: float
    initial_velocity: float
    entry_angle_degree: float
    median_residual_arcsec: float
    quality_angle_q: float

class TrajectoryResponse(BaseModel):
    startLat: float
    startLng: float
    startAltKm: float
    endLat: float
    endLng: float
    endAltKm: float
    mass: float
    initial_velocity: float
