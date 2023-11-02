def solution():
    # Define initial number of weasels and rabbits
    initial_weasels = 100
    initial_rabbits = 50

    # Calculate number of weasels and rabbits caught by each fox per week
    weasels_per_fox_per_week = 4
    rabbits_per_fox_per_week = 2

    # Calculate total number of weasels and rabbits caught per week by all foxes
    total_weasels_caught_per_week = 3 * weasels_per_fox_per_week
    total_rabbits_caught_per_week = 3 * rabbits_per_fox_per_week

    # Calculate number of weasels and rabbits caught over 3 weeks
    weasels_caught = total_weasels_caught_per_week * 3
    rabbits_caught = total_rabbits_caught_per_week * 3

    # Calculate final number of weasels and rabbits
    final_weasels = initial_weasels - weasels_caught
    final_rabbits = initial_rabbits - rabbits_caught

    # Return a tuple containing the final number of weasels and rabbits
    result = (final_weasels, final_rabbits)
    return result

print(solution())