def calculate_risk_score(
    rainfall,
    soil_moisture,
    slope,
    humidity
):
    # Convert rainfall to score (0-100)
    rainfall_score = min((rainfall / 200) * 100, 100)

    # Soil moisture score
    moisture_score = min(soil_moisture, 100)

    # Slope score
    slope_score = min((slope / 60) * 100, 100)

    # Humidity score
    humidity_score = min(humidity, 100)

    # Weighted risk score
    risk_score = (
        rainfall_score * 0.35 +
        moisture_score * 0.30 +
        slope_score * 0.20 +
        humidity_score * 0.15
    )

    risk_score = round(risk_score, 2)

    # Risk level
    if risk_score < 35:
        risk_level = "Low"
    elif risk_score < 65:
        risk_level = "Medium"
    else:
        risk_level = "High"

    return risk_score, risk_level


# Test values
rainfall = 130
soil_moisture = 88
slope = 44
humidity = 90

score, level = calculate_risk_score(
    rainfall,
    soil_moisture,
    slope,
    humidity
)

print("================================")
print("LANDSLIDE RISK SCORE")
print("================================")

print("Rainfall:", rainfall)
print("Soil Moisture:", soil_moisture)
print("Slope:", slope)
print("Humidity:", humidity)

print("\nRisk Score:", score, "/ 100")
print("Risk Level:", level)

print("================================")