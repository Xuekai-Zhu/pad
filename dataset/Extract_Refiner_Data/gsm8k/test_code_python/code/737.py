def solution():
    
    # Define the initial number of birds
    initial_birds = 12

    # Calculate the number of birds scared away
    scared_away = initial_birds // 3

    # Calculate the number of birds left after scaring away
    remaining_birds = initial_birds - scared_away

    # Calculate the number of birds that joined the fearless birds
    joined_fearless_birds = 20

    # Calculate the total number of birds in the backyard
    total_birds = remaining_birds + joined_fearless_birds

    # Display the total number of birds in the backyard
    result = total_birds
    return result

print(solution())