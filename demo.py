from fastapi import FastAPI, HTTPException
from typing import List
import pandas as pd

app = FastAPI()

df = pd.read_csv('POPS.csv')

if 'State' not in df.columns or 'City' not in df.columns:
    raise Exception("CSV must have 'State' and 'City' columns")

df = df.dropna(subset=['State', 'City'])

df['State'] = df['State'].str.strip()
df['City'] = df['City'].str.strip()

@app.get( "/states/{letter}")
def get_states(letter: str):
    letter = letter.upper()
    filtered_states = df[df['State'].str.upper().str.startswith(letter)]['State'].unique().tolist()

    if not filtered_states:
        raise HTTPException(status_code=404, detail="No states found starting with that letter")
    return sorted(filtered_states)

@app.get("/cities/{state_name}")
def get_cities(state_name: str):
    filtered_cities = df[df['State'].str.lower() == state_name.lower()]['City'].unique().tolist()

    if not filtered_cities:
        raise HTTPException(status_code=404, detail="No cities found for this state")
    return sorted(filtered_cities)

@app.get("/details/{state_name}/{city_name}")
def get_cities(state_name: str, city_name: str):
    filtered_data = df[(df['State'].str.lower() == state_name.lower()) & (df['City'].str.lower() == city_name.lower())]

    if filtered_data.empty:
        raise HTTPException(status_code=404, detail="No data found for this state and city")
    return filtered_data.to_dict()