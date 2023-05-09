
class Characteristics:
    '''creates characteristics object using data pulled from animal object with get_data method in another file'''
    def __init__(self, data1):
        self.characteristics = data1[0]['characteristics']