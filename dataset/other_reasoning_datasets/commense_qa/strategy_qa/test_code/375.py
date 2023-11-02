def solution():
    # Define the length of the Titanic deck and the length of a giant squid
    titanic_deck_length = 500
    giant_squid_length = 59
    # Check if the giant squid would fit on the Titanic deck
    if giant_squid_length <= titanic_deck_length:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())