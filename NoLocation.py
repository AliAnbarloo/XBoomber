import phonenumbers
from phonenumbers import geocoder


MayNotSend = ["Afghanistan","Algeria","Benin","Burkina Faso","Cameroon","Central African Republic","Chad","Colombia","Democratic","Ethiopia","Ghana","Iraq","Ivory","Libya","Mali","Mauritania","Mexico","Mozambique","Myanmar","Niger","Nigeria","Russia","Somalia","South Sudan","Syria","Tanzania","Togo","Tunisia","Uganda","Ukraine","Liberia","Malawi","Congo","Burundi"]
NotSend =["Yemen","Palestine","Lebanon"]


def country(phone_number:int) -> str:
    try:
        number = phonenumbers.parse(phone_number)
        location = geocoder.description_for_number(number, 'fa')
    except:
        location = "Err"
    finally:
        return location

def location_status(no_location:str) -> str:
    if no_location=="Iran":
        return "Iran"
    elif no_location=="Err":
        return "Err"
    elif no_location in MayNotSend:
        return "warning"
    elif no_location in NotSend:
        return "No"
    else:
        return "Ok"

if __name__ == '__main__':
    example_number = "+380945225372"
    location_of_number = country(example_number)
    status = location_status(location_of_number)
    print(location_of_number )
    print(status)