def solution():
    # Define Asiana Airlines as a real airline and Harry Potter as a fictional character
    asiana_airlines_real = True
    harry_potter_fictional = True
    # Check if Harry Potter can book a flight on Asiana Airlines
    if asiana_airlines_real and not harry_potter_fictional:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())