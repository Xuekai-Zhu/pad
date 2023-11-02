def solution():
    """Samara and three of her friends heard alligators spotted on the local river and decided to join a search organized by the wildlife service to capture the animals. After searching the whole day, Samara had seen 20 alligators while her friends had seen an average of 10 alligators each. Calculate the total number of alligators Samara and her friends saw."""
    # Define the number of friends
    num_friends = 3

    # Calculate the number of alligators seen by Samara's friends
    friends_alligators = num_friends * 10

    # Calculate the total number of alligators seen
    total_alligators = friends_alligators + 20

    # return the result
    result = total_alligators
    return result

print(solution())