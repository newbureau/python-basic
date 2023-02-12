import json
from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/ping/")
def read_ping():
    # return json.dumps({"hello": "root"})
    return Response(
        content=json.dumps({"message": "pong"}),
        media_type="application/json",
    )
