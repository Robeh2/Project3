
class Locations:
    '''creates locations object using data pulled from animal object with get_data method in another file'''
    def __init__(self, data1):
        self.locations = data1[0]['locations']

