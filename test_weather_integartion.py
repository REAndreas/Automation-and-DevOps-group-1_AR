import pytest
import pandas as pd
from unittest.mock import patch
from datetime import datetime, timedelta

from weather_api_call import get_weather  

@patch("weather_api_call.requests.get")
def test_get_weather_returns_dataframe(mock_get):
    """Test that get_weather returns a filtered DataFrame with correct columns."""

    
    now = datetime.now()
    
    times = pd.date_range(now - timedelta(hours=5), now + timedelta(hours=43), freq="1h").strftime("%Y-%m-%dT%H:%M").tolist()
    temps = list(range(len(times)))

    mock_response = {
        "hourly": {
            "time": times,
            "temperature_2m": temps
        }
    }

    mock_get.return_value.json.return_value = mock_response


    df = get_weather()


    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ["time", "temperature"]
    assert not df.empty
    assert len(df["time"]) == 24


    min_time, max_time = df["time"].min(), df["time"].max()
    assert min_time >= now - timedelta(minutes=1)  
    assert max_time <= now + timedelta(hours=24, minutes=1)