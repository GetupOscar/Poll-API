import os
import redis
from fastapi import FastAPI
from pydantic import BaseModel

class RenderInfo(BaseModel): renderOnPC: int

app = FastAPI()
conn = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses = True
)

@app.get("/get-flag")
def get_flag():
    if not conn.exists("renderOnPC"): return {"renderOnPC": -1} 
    return {"renderOnPC": conn.get('renderOnPC')} 

@app.post("/update-flag")
def update_flag(info: RenderInfo):
    conn.set("renderOnPC", info.renderOnPC)
    return {"renderOnPC": conn.get('renderOnPC')}
