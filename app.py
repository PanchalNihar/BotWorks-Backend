from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
from typing import Optional
from geopy.geocoders import Nominatim

# ----------------------------
# Load trained model
# ----------------------------
MODEL_PATH = "solar_power_model.pkl"
try:
    model = joblib.load(MODEL_PATH)   # trained on 6 features
except Exception as e:
    model = None
    print("⚠️ Could not load model:", e)

# ----------------------------
# Initialize FastAPI + Geocoder
# ----------------------------
app = FastAPI(title="Solar Power Prediction API")
geolocator = Nominatim(user_agent="solar_predictor")

# ----------------------------
# Input Schema
# ----------------------------
class PredictionInput(BaseModel):
    location: Optional[str] = None   # Optional: City/Place
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    shortwave_radiation_backwards_sfc: float
    azimuth: float
    zenith: float
    angle_of_incidence: float

# ----------------------------
# Helper: Get lat/lon from location
# ----------------------------
def get_coordinates_from_location(location: str):
    try:
        loc = geolocator.geocode(location)
        if loc:
            return loc.latitude, loc.longitude
        return None, None
    except Exception:
        return None, None

# ----------------------------
# Endpoints
# ----------------------------
@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Solar Power Prediction API. POST to /predict with location or lat/lon."
    }

@app.post("/predict")
async def predict(input: PredictionInput):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not available. Train it first.")

    # Resolve coordinates
    lat, lon = input.latitude, input.longitude
    if input.location and (lat is None or lon is None):
        lat, lon = get_coordinates_from_location(input.location)
        if lat is None or lon is None:
            raise HTTPException(status_code=400, detail="Could not resolve location to coordinates.")

    if lat is None or lon is None:
        raise HTTPException(status_code=400, detail="Either provide latitude+longitude or a valid location.")

    # Build feature vector (exactly the same 6 features used in training)
    features = {
        "latitude": lat,
        "longitude": lon,
        "shortwave_radiation_backwards_sfc": input.shortwave_radiation_backwards_sfc,
        "azimuth": input.azimuth,
        "zenith": input.zenith,
        "angle_of_incidence": input.angle_of_incidence
    }

    # Predict
    try:
        X = pd.DataFrame([features])
        pred = model.predict(X)
        return {
            "latitude": lat,
            "longitude": lon,
            "predicted_generated_kw": float(pred[0])
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {e}")

# ----------------------------
# Run locally
# ----------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
