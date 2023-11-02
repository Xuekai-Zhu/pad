def solution():
    green_leaves_per_plant = 18
    fraction_of_leaves_remaining = 2/3

    # Calculate the total number of green leaves on all three plants
    total_green_leaves = 3 * green_leaves_per_plant

    # Calculate the number of green leaves that fall off each plant
    leaves_lost_per_plant = green_leaves_per_plant * (1/3)

    # Calculate the total number of green leaves remaining on all three plants
    total_green_leaves_remaining = total_green_leaves * fraction_of_leaves_remaining

    # Subtract the number of lost leaves to get the final answer
    final_answer = total_green_leaves_remaining - leaves_lost_per_plant
    return final_answer

print(solution())