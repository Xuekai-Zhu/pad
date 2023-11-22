def solution():
    
    # Define the number of birds attracted by each bird feeder
    birds_per_feeder = 20

    # Define the number of feeders Lillian has
    num_feeders = 4

    # Calculate the total number of birds attracted by the feeders
    total_birds = birds_per_feeder * num_feeders

    # Calculate the number of birds attracting 10 more birds than the store-bought ones
    additional_birds = 10 * 20

    # Calculate the total number of birds attracting more birds
    total_birds -= additional_birds

    # Display the total number of birds attracting
    result = total_birds
    return result

print(solution())