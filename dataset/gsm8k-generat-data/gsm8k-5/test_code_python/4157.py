def solution():
    flour_per_biscuit = 1.25 / 9  # Lady Bird uses 1 1/4 cup flour to make 9 biscuits
    biscuits_per_guest = 2  # Lady Bird wants to allow 2 biscuits per guest
    guests = 18  # The Junior League club has 18 members

    # Calculate the total flour needed for all the biscuits
    total_flour = flour_per_biscuit * biscuits_per_guest * guests

    result = total_flour
    return result

print(solution())