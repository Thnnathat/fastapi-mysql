from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

from activity import Activity

activity = Activity()
app = FastAPI()

class Update(BaseModel):
    Id : int
    name: str
    Type: str

@app.get("/hardware/update")
async def update_hw(Id, status, value):
    data = activity.update_hw(Id, status, value)
    return data

@app.post("/hardware/post_update")
async def post_update(update: Update):
    data = activity.update_post(update.Id, update.name, update.Type)
    return data

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)