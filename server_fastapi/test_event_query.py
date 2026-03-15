import asyncio
import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

async def test_event_query():
    """Test the event query directly"""
    mongo_uri = os.getenv("MONGODB_URI")
    
    client = AsyncIOMotorClient(mongo_uri)
    db = client["AstrathonDb"]
    
    try:
        collection = db["events"]
        
        # Test 1: Empty query
        print("Test 1: Empty query")
        results = []
        async for event in collection.find({}):
            results.append(event)
        print(f"  Found {len(results)} events")
        
        # Test 2: Search for PER
        print("\nTest 2: Search for 'PER' in shower_code or region")
        query = {
            "$or": [
                {"shower_code": {"$regex": "PER", "$options": "i"}},
                {"region": {"$regex": "PER", "$options": "i"}}
            ]
        }
        results = []
        async for event in collection.find(query):
            results.append(event)
        print(f"  Found {len(results)} events")
        if results:
            print(f"  Sample: {results[0]}")
            
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(test_event_query())
