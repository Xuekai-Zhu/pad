def solution():
    # Calculate the number of fish the Bobbit worm ate in two weeks
    eaten_in_two_weeks = 2 * 14  # The worm eats 2 fish per day for 14 days

    # Subtract the eaten fish from the total number of fish
    remaining_fish = 60 - eaten_in_two_weeks

    # Add the 8 fish James added a week after the worm started eating
    total_fish = remaining_fish + 8

    result = total_fish
    return result

print(solution())