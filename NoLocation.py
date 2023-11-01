import phonenumbers
from phonenumbers import geocoder


def country(phone_number:int) -> str:
    try:
        number = phonenumbers.parse(phone_number)
        location = geocoder.description_for_number(number, 'fa')
    except:
        location = "Err"
    finally:
        return location


if __name__ == '__main__':
    example_number = "+380945225372"
    location_of_number = country(example_number)
    print(location_of_number )