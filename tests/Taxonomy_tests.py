import pytest
from Taxonomy import Taxonomy

@pytest.fixture
def data():
    return [{"taxonomy": {
      "kingdom": "Animalia",
      "phylum": "Chordata",
      "class": "Mammalia",
      "order": "Carnivora",
      "family": "Felidae",
      "genus": "Panthera",
      "scientific_name": "Panthera onca"
    }}]

def test_taxonomy(data):
    taxonomy = Taxonomy(data)
    assert taxonomy.taxonomy == {'kingdom': 'Animalia', 'phylum': 'Chordata', 'class': 'Mammalia', 'order': 'Carnivora', 'family': 'Felidae', 'genus': 'Panthera', 'scientific_name': 'Panthera onca'}
