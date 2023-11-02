def solution():
    """Lenny bought 20 boxes of pens. Each box contained 5 pens. She gave 40% of the pens to her close friends and one-fourth of what's left to her classmates. How many pens were left for Lenny?"""
    # Define the initial number of pens
    pens = 20 * 5

    # Calculate the number of pens given to close friends
    friends_pens = pens * 0.4

    # Calculate the number of pens remaining
    remaining_pens = pens - friends_pens

    # Calculate the number of pens given to classmates
    classmates_pens = remaining_pens * 0.25

    # Calculate the number of pens left for Lenny
    left_pens = remaining_pens - classmates_pens

    result = left_pens
    return result

print(solution())