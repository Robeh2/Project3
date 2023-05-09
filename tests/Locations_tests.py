import pytest
from Locations import Locations

@pytest.fixture
def data1():
    return [{"locations": [
        "Central-America",
        "South-America"
    ]}]
@pytest.fixture
def data2():
    return [{"locations": [
      "Africa",
      "Asia",
      "Central-America",
      "Eurasia",
      "Europe",
      "North-America",
      "Oceania",
      "South-America"
    ]}]
@pytest.fixture
def data3():
    return [{"locations": [
        "North-America",
        "Oceania",
        "Africa",
        "Asia"
    ]}]
def test_locations():
    locations1 = Locations(data1)
    locations2 = Locations(data2)
    locations3 = Locations(data3)
    assert locations1.locations == [
        "Central-America",
        "South-America"
    ]
    assert locations2.locations == [
      "Africa",
      "Asia",
      "Central-America",
      "Eurasia",
      "Europe",
      "North-America",
      "Oceania",
      "South-America"
    ]
    assert locations3.locations == [
        "North-America",
        "Oceania",
        "Africa",
        "Asia"
    ]
