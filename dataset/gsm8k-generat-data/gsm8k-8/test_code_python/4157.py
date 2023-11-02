def solution():
    # Calculate how much flour is needed for 1 biscuit
    flour_per_biscuit = 1.25 / 9

    # Calculate how much flour is needed for 2 biscuits per guest
    flour_per_guest = flour_per_biscuit * 2

    # Calculate how much flour is needed for all guests
    total_flour = flour_per_guest * 18

    result = round(total_flour, 2) # round to 2 decimal places
    return result

print(solution())