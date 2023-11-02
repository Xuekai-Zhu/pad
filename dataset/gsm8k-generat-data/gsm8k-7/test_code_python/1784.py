def solution():
    starting_chips = 22
    brother_chips = 7
    sister_chips = 5

    # Calculate the total number of chips given away
    total_given_away = brother_chips + sister_chips

    # Calculate the number of chips Nancy kept for herself
    remaining_chips = starting_chips - total_given_away
    result = remaining_chips
    return result

print(solution())