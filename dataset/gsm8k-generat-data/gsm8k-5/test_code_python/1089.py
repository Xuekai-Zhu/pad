def solution():
    starting_cans = 12 # Coleen started with 12 cans
    final_cans = (starting_cans / 2) - 3 # Coleen ended up with 3 less than half as many cans as she started with

    # Calculate the number of cans of sprinkles remaining
    remaining_cans = starting_cans - final_cans
    result = remaining_cans
    return result

print(solution())