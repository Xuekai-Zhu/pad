def solution():
    num_water_bottles = 4 * 12  # Four dozen bottles
    num_players = 11
    initial_take = 2  # Bottles taken in the first break
    final_take = 1  # Bottles taken after the game

    # Calculate the total number of bottles taken
    total_take = num_players * (initial_take + final_take)

    # Calculate the number of bottles remaining
    bottles_remaining = num_water_bottles - total_take
    result = bottles_remaining
    return result

print(solution())