@app.post("/predict")
def predict(data: LandslideData):

    input_data = pd.DataFrame([{
        "rainfall": data.rainfall,
        "soil_moisture": data.soil_moisture,
        "slope": data.slope,
        "temperature": data.temperature,
        "elevation": data.elevation,
        "humidity": data.humidity
    }])

    # ML prediction
    ml_prediction = model.predict(input_data)[0]

    # Risk score
    risk_score, risk_level = calculate_risk_score(
        data.rainfall,
        data.soil_moisture,
        data.slope,
        data.humidity
    )

    return {
        "ml_prediction": ml_prediction,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "warning": (
            "HIGH LANDSLIDE RISK!"
            if risk_level == "High"
            else "No immediate high-risk warning."
        )
    }