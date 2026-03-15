import asyncio
import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

async def list_collections():
    """List all collections in the database"""
    mongo_uri = os.getenv("MONGODB_URI")
    print(f"Connecting to: {mongo_uri[:50]}...")
    
    client = AsyncIOMotorClient(mongo_uri)
    db = client["AstrathonDb"]
    
    try:
        # Get list of collections
        collections = await db.list_collection_names()
        print(f"\nCollections in 'AstrathonDb' database:")
        for coll in collections:
            count = await db[coll].count_documents({})
            print(f"  - {coll} ({count} documents)")
        
        # Try to query events specifically
        if "events" in collections:
            events_count = await db["events"].count_documents({})
            print(f"\nEvents collection has {events_count} documents")
            # Show sample
            sample = await db["events"].find_one()
            print(f"Sample event: {sample}")
        else:
            print("\n✗ 'events' collection not found!")
            
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(list_collections())
