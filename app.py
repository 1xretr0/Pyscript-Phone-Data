from xml.dom.minidom import Element
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

phone_number = Element("phone-input")

def searchPhoneData(*ags, **kws):
    # ignore empty phone number
    if not phone_number.element.value:
        return None

    # e.g. +522223391262
    # mobileNumber = input("Enter mobile number with country code: ")
    mobileNumber = phonenumbers.parse(phone_number.element.value)

    # get timezone of a phone number
    phone_timezone = timezone.time_zones_for_number(mobileNumber)

    # get carrier of a phone number
    # phone_carrier = carrier.name_for_number(mobileNumber, 'en')

    # get region info
    phone_region = geocoder.description_for_number(mobileNumber, 'en')

    # validating phone number
    phone_validation = phonenumbers.is_valid_number(mobileNumber)

    # checking possibility of a number
    phone_possibility = phonenumbers.is_possible_number(mobileNumber)

    pyscript.write('phone', phone_number)
    pyscript.write('timezone', phone_timezone)
    pyscript.write('region', phone_region)
    pyscript.write('valid', phone_validation)
    pyscript.write('possibility', phone_possibility)


def searchPhoneDataEvent(e):
    if e.key == "Enter":
        searchPhoneData()

phone_number.element.onkeypress = searchPhoneDataEvent