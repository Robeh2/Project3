import pytest
from Name import Name

@pytest.fixture
def data():
    return [
  {
    "name": "Jaguar",
    "taxonomy": {
      "kingdom": "Animalia",
      "phylum": "Chordata",
      "class": "Mammalia",
      "order": "Carnivora",
      "family": "Felidae",
      "genus": "Panthera",
      "scientific_name": "Panthera onca"
    },
    "locations": [
      "Central-America",
      "South-America"
    ],
  },
]

def test_name(data):
    name = Name(data)
    assert name.name == 'Jaguar'