def solution():
    """Lenny bought 20 boxes of pens. Each box contained 5 pens. She gave 40% of the pens to her close friends and one-fourth of what's left to her classmates. How many pens were left for Lenny?"""
    # Define the number of pens per box
    PENS_PER_BOX = 5

    # Calculate the total number of pens Lenny bought
    total_pens = 20 * PENS_PER_BOX

    # Calculate the number of pens Lenny gave to her friends
    pens_to_friends = int(total_pens * 0.4)

    # Calculate the number of pens left after giving to friends
    pens_left = total_pens - pens_to_friends

    # Calculate the number of pens Lenny gave to her classmates
    pens_to_classmates = int(pens_left / 4)

    # Calculate the number of pens left for Lenny
    pens_left_for_lenny = pens_left - pens_to_classmates

    # Display the number of pens left for Lenny
    result = pens_left_for_lenny
    return result

print(solution())