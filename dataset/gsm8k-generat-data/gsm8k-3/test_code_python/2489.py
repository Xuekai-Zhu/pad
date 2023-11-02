def solution():
    """Samara and three of her friends heard alligators spotted on the local river and decided to join a search organized by the wildlife service to capture the animals. After searching the whole day, Samara had seen 20 alligators while her friends had seen an average of 10 alligators each. Calculate the total number of alligators Samara and her friends saw."""
    # Define the number of friends
    NUM_FRIENDS = 3

    # Define the number of alligators Samara saw
    samara_alligators = 20

    # Define the average number of alligators seen by her friends
    friend_alligators = 10

    # Calculate the total number of alligators seen
    total_alligators = samara_alligators + (NUM_FRIENDS * friend_alligators)

    # Display the total number of alligators seen
    result = total_alligators
    return result

print(solution())