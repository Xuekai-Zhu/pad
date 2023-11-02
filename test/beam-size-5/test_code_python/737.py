def solution():
    
    # Define the initial number of birds
    initial_birds = 12

    # Calculate the number of birds scaring away
    scaring_away = initial_birds * (1/3)

    # Calculate the number of birds after the stone
    final_birds = initial_birds - scaring_away + 20

    # Display the final number of birds
    result = final_birds
    return result

print(solution())