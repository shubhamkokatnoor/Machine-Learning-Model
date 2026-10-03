from fastapi import FastAPI
import joblib
import uvicorn

app = FastAPI()

myAi = joblib.load("./models/MyAi.pkl")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/myai")
def price_prediction(data:dict):
    params = [[
        data["Area_sqft"],
        data["Bedrooms"],
        data["Bathrooms"]
        ]]
    res = myAi.predict(params)[0]
    print(res)


    return{
        "House Price In Lakh":f"{res}"
        }

