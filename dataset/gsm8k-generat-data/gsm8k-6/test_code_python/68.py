def solution():
    # Find the number of coins that Elsa has
    elsa_share = (10/55) * 440  # the ratio of Elsa's coins to the total is 10/55

    # Find the number of coins that Amalie has
    amalie_share = (45/55) * 440  # the ratio of Amalie's coins to the total is 45/55

    # Calculate the coins Amalie has remaining after spending 3/4
    amalie_remaining = (1 - (3/4)) * amalie_share

    result = amalie_remaining
    return result

print(solution())