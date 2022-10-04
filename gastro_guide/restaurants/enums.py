from enumchoicefield import ChoiceEnum


class CategoryEnum(ChoiceEnum):
    CAFE = 'cafe'
    RESTAURANT = 'restaurant'
    COFFE_HOUSE = 'coffe house'
    PUB = 'pub'
    BAR = 'bar'
    OTHER = 'other'


class CuisineEnum(ChoiceEnum):
    ASIAN = 'asian'
    AMERICAN = 'american'
    NATIONAL = 'national'
    VEGETERIAN = 'vegeterian'
    OTHER = 'other'
