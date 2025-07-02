from fastapi import FastAPI, HTTPException, Query
import pandas as pd

app = FastAPI()

df = pd.read_csv('POPS.csv')

if 'State' not in df.columns or 'City' not in df.columns:
    raise Exception("CSV must have 'State' and 'City' columns")

df = df.dropna(subset=['State', 'City'])

df['State'] = df['State'].str.strip().str.title()
df['City'] = df['City'].str.strip().str.title()

@app.get( "/states")
def get_states(letter: str=Query(..., min_length=1, max_length=3, description="First letter of the state")):
    letter = letter.strip().title()
    filtered_states = df[df['State'].str.startswith(letter)]['State'].drop_duplicates().tolist()

    if len(filtered_states) == 0:
        raise HTTPException(status_code=404, detail="No states found starting with that letter")
    
    return sorted(filtered_states)

@app.get("/cities")
def get_cities(state_name: str=Query(..., description="Name of the state")):
    state_name = state_name.strip().title()
    filtered_cities = df[df['State'] == state_name]['City'].drop_duplicates().tolist()

    if len(filtered_cities) == 0:
        raise HTTPException(status_code=404, detail="No cities found for this state")
    
    return sorted(filtered_cities)

@app.get("/details")
def get_cities(state_name: str=Query(..., description="Name of the state"), city_name: str=Query(..., description="Name of the city")):
    state_name = state_name.strip().title()
    city_name = city_name.strip().title()
    filtered_data = df[(df['State']== state_name) & (df['City']== city_name)]

    if filtered_data.empty:
        raise HTTPException(status_code=404, detail="No data found for this state and city")
    
    return filtered_data.to_dict('records')