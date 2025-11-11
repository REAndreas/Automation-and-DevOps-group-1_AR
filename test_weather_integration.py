import pytest
import pandas as pd
from weather_api_call import get_weather

@pytest.mark.integration
def test_get_weather_real_api():
    """Integration test: calls the real Open-Meteo API and checks structure of response."""

    df = get_weather()


    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert list(df.columns) == ["time", "temperature"]

    assert pd.api.types.is_datetime64_any_dtype(df["time"])
    assert pd.api.types.is_numeric_dtype(df["temperature"])