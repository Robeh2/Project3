from Animal import Animal
from flask import Flask, request
import json

app = Flask(__name__)
'''creates search history route, to allow user to see what animals they have looked at during their session'''
@app.route('/search-history', methods = ['GET','POST'])
def search_history():
    return_button = '<form action="/" method="get">' \
                     '<button type="submit" style="font-size: 40px;">Return to Home</button></form>'
    with open('animals_bank.json', 'r') as f:
        animals = sorted(json.load(f))
    history = '<br>\n'.join(animal.capitalize() for animal in animals)
    history_text = f'<body style="background-color: #333; color: #fff; text-align: center;"><div style="text-align: center; ' \
           f'font-size: 50px; background-color: #333; color: #fff;"><h2>Animal Search History:</h2></div></body>\n{history}'
    return f'<body style="background-color: #333; color: #fff; text-align: center;"><div style="text-align: center; ' \
           f'font-size: 30px; background-color: #333; color: #fff;"><h2>{history_text}<br><br>{return_button}</h2></div></body>'
'''creates home_page route wher user can being using the site'''
@app.route('/', methods=['GET', 'POST'])
def start_page():
    '''creates return button for user to be able to return to main page from any other page'''
    return_button = '<form action="/" method="get">' \
                    '<button type="submit" style="font-size: 40px;">Return to Home</button></form>'
    '''creates history button for user to be able to see search history from any page'''
    history_button = '<form action="/search-history" method="get">' \
                     '<button type="submit" style="font-size: 40px;">Search History</button></form>'
    '''initializes objects and allows user to enter an animal to see. uses 
        json to store animals in a file for search history'''
    if request.method == 'POST':
        animal_name = request.form['animal_name']
        animal_object = Animal(animal_name)
        animals = []
        data1 = animal_object.get_data()
        name = animal_object.get_name(data1)
        with open('animals_bank.json', 'r') as f:
            data = f.read()
            if data.strip():
                animals = json.loads(data)
        if animal_name not in animals:
            animals.append(name.name)
            with open('animals_bank.json', 'w') as f:
                json.dump(animals, f)
        '''checks if animal exists. if not, gives user message that it does not exitst.'''
        if not data1:
            return f'<body style="background-color: #333; color: #fff; text-align: center;"><div style="text-align: ' \
                   f'center; font-size: 60px; background-color: #333; color: #fff;"><h2>' \
                   f'Sorry, {animal_name.capitalize()} does not exist!<br>{return_button}</h2></div></body>'
        taxonomy = animal_object.get_taxonomy(data1)
        taxonomy_str = ''
        for key, value in taxonomy.taxonomy.items():
            taxonomy_str += f"<br>{key.capitalize()}: {value}"
        locations = animal_object.get_locations(data1)
        characteristics = animal_object.get_characteristics(data1)
        characteristics_str = ""
        for key, value in characteristics.characteristics.items():
            characteristics_str += f"<br>{key.capitalize()}: {value}"
        info_type = request.form['info_type']
        '''displays taxonomy ,locations, and characteristics info based on what user chooses, as well as the buttons'''
        if info_type == 'taxonomy':
            return f'<body style="background-color: #333; color: #fff; text-align: center;"><div style="text-align: ' \
                   f'center; font-size: 45px; background-color: #333; color: #fff;"><h2>Animal ' \
                   f'Taxonomy</h2><p>{taxonomy_str}{history_button}{return_button}</div></body>'
        elif info_type == 'locations':
            combined = "<br>".join(locations.locations)
            return f'<body style="background-color: #333; color: #fff; text-align: center;"><div style="text-align: ' \
                   f'center; font-size: 45px; background-color: #333; color: #fff;"><h2>Animal Locations<' \
                   f'/h2><p>{combined}</p></div>{history_button}{return_button}</body>'
        elif info_type == 'characteristics':
            return f'<body style="background-color: #333; color: #fff; text-align: center;"><div style="text-align: ' \
                   f'center; font-size: 45px; background-color: #333; color: #fff;"><h2>Animal ' \
                   f'Characteristics</h2><p>{characteristics_str}{history_button}{return_button}</div></body>'
    else:
        return '''
        <!DOCTYPE html>
<html>
  <head>
    <title>Animal Information</title>
    <style>
      @font-face {
        font-family: 'Bebas Neue';
        src: url('/path/to/BebasNeue-Regular.ttf') format('truetype');
      }
      body {
        font-family: 'Bebas Neue', sans-serif;
      }
    </style>
  </head>
  <body style="background-color: #333; color: #fff; text-align: center;">
    <h1 style="font-size: 50px; color: white;">WELCOME TO ANIMAL INFO!<br>NAME AN ANIMAL, AND SEE INFORMATION ABOUT IT!</h1>
    <h2 style="font-size: 30px; color: white;">(Be very specific, there are different types of foxes!)</h2>
    <form method="post">
      <label for="animal_name" style="font-size: 60px; color: #E8E5E4;">Enter Animal Name:</label><br>
      <input type="text" id="animal_name" name="animal_name" style="font-size: 60px;"><br>
      <label for="info_type" style="font-size: 60px; color: #E8E5E4;">Select Information:</label><br>
      <select id="info_type" name="info_type" style="font-size: 60px;">
        <option value="taxonomy">Taxonomy</option>
        <option value="locations">Locations</option>
        <option value="characteristics">Characteristics</option>
      </select><br><br>
      <input type="submit" value="Submit" style="font-size: 60px;">
      <button type="submit" formaction="/search-history" style="font-size: 60px;">Search History</button>
    </form>
  </body>
</html>
'''
'''the above html block creates the homepage for users to start from after which they can make their choices'''
if __name__ == '__main__':
    app.run()

