def solution():
    # Calculate the total number of people that can ride in one turn
    people_per_turn = 7 * 2

    # Calculate the number of turns needed to give everyone a turn
    turns_needed = 84 / people_per_turn

    # Round up to the nearest whole number
    turns_needed = math.ceil(turns_needed)

    result = turns_needed
    return result

print(solution())