import phonenumbers
from phonenumbers import geocoder


def country(phone_number:int) -> str:
    number = phonenumbers.parse(phone_number)
    location = geocoder.description_for_number(number, 'fa')
    return location


if __name__ == '__main__':
    example_number = "+380945225372"
    location_of_number = country(example_number)
    print(location_of_number )