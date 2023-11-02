def solution():
    
    # Define the number of birds Lillian builds and buys
    birds_built = 3
    birds_bought = 3

    # Calculate the total number of birds Lillian has
    total_birds = (birds_built + birds_bought) * 2

    # Calculate the number of birds Lillian can prefer the feeders
    birds_prefered = total_birds + 10

    # Calculate the number of birds Lillian can expect to see in her garden each day
    birds_per_day = total_birds - birds_prefered

    # Display the number of birds Lillian can expect to see in her garden each day
    result = birds_per_day
    return result

print(solution())