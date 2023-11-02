def solution():
    """Ten boys brought 15 popsicle sticks each. Twelve girls brought 12 popsicle sticks each. How many fewer popsicle sticks did the girls bring than the boys?"""
    # Calculate the total number of popsicle sticks brought by the boys
    boys_popsicle_sticks = 10 * 15

    # Calculate the total number of popsicle sticks brought by the girls
    girls_popsicle_sticks = 12 * 12

    # Calculate the difference between the two totals
    difference = boys_popsicle_sticks - girls_popsicle_sticks

    # Return the result
    result = difference
    return result

print(solution())