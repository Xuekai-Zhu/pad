def solution():
    """To eat to when she gets full, Michaela needs 20 oranges. Cassandra needs twice as many oranges as Michaela to eat until she gets full. If they picked 90 oranges from the farm today, how many oranges would remain after they've both eaten until they were full?"""
    # Define the number of oranges Michaela needs to get full
    michaela_oranges = 20

    # Calculate the number of oranges Cassandra needs to get full
    cassandra_oranges = michaela_oranges * 2

    # Define the total number of oranges picked from the farm
    total_oranges = 90

    # Calculate the number of oranges remaining after they've both eaten until they were full
    remaining_oranges = total_oranges - (michaela_oranges + cassandra_oranges)

    # Display the number of oranges remaining
    result = remaining_oranges
    return result

print(solution())