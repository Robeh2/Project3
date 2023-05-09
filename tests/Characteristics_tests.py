import pytest
from Characteristics import Characteristics

@pytest.fixture
def data():
    return [{"characteristics": {
      "prey": "Deer, Capybara, Tapir",
      "name_of_young": "Cub",
      "group_behavior": "Solitary",
      "estimated_population_size": "15,000",
      "biggest_threat": "Hunting and habitat loss",
      "most_distinctive_feature": "Beautiful rosetted fur pattern",
      "gestation_period": "90 - 105 days",
      "habitat": "Rainforest, swamp and floodplains",
      "diet": "Carnivore",
      "average_litter_size": "3",
      "lifestyle": "Crepuscular",
      "common_name": "Jaguar",
      "number_of_species": "1",
      "location": "Central and South America",
      "slogan": "The largest feline on the American continent!",
      "group": "Mammal",
      "color": "BrownYellowBlackWhiteTan",
      "skin_type": "Fur",
      "top_speed": "50 mph",
      "lifespan": "12 - 15 years",
      "weight": "36kg - 160kg (79lbs - 350lbs)",
      "length": "1.1m - 1.9m (43in - 75in)",
      "age_of_sexual_maturity": "3 - 4 years",
      "age_of_weaning": "3 months"
    }}]

def test_taxonomy(data):
    characteristics = Characteristics(data)
    assert characteristics.characteristics == {
      "prey": "Deer, Capybara, Tapir",
      "name_of_young": "Cub",
      "group_behavior": "Solitary",
      "estimated_population_size": "15,000",
      "biggest_threat": "Hunting and habitat loss",
      "most_distinctive_feature": "Beautiful rosetted fur pattern",
      "gestation_period": "90 - 105 days",
      "habitat": "Rainforest, swamp and floodplains",
      "diet": "Carnivore",
      "average_litter_size": "3",
      "lifestyle": "Crepuscular",
      "common_name": "Jaguar",
      "number_of_species": "1",
      "location": "Central and South America",
      "slogan": "The largest feline on the American continent!",
      "group": "Mammal",
      "color": "BrownYellowBlackWhiteTan",
      "skin_type": "Fur",
      "top_speed": "50 mph",
      "lifespan": "12 - 15 years",
      "weight": "36kg - 160kg (79lbs - 350lbs)",
      "length": "1.1m - 1.9m (43in - 75in)",
      "age_of_sexual_maturity": "3 - 4 years",
      "age_of_weaning": "3 months"
    }