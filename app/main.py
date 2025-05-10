from fastapi import FastAPI

app = FastAPI()

# Include routers here
# from app.routers import some_router
# app.include_router(some_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}