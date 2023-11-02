def solution():
    # Define the number of oranges Michaela needs
    michaela_oranges = 20

    # Define the number of oranges Cassandra needs
    cassandra_oranges = 2 * michaela_oranges

    # Calculate the total number of oranges they need
    total_oranges = michaela_oranges + cassandra_oranges

    # Calculate the number of oranges left after they eat until full
    oranges_left = 90 - total_oranges

    result = oranges_left
    return result

print(solution())