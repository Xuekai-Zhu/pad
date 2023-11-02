def solution():
    # Calculate how many fish were eaten by the Bobbit worm in two weeks
    days_in_two_weeks = 14
    fish_eaten_in_two_weeks = 2 * days_in_two_weeks
    remaining_fish = 60 - fish_eaten_in_two_weeks

    # Add the 8 new fish
    remaining_fish += 8

    # Calculate how many fish were eaten by the Bobbit worm in the final week
    days_in_final_week = 7
    fish_eaten_in_final_week = 2 * days_in_final_week

    # Subtract the final week's fish loss from the remaining fish
    final_fish_count = remaining_fish - fish_eaten_in_final_week
    result = final_fish_count
    return result

print(solution())