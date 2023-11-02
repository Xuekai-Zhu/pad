def solution():
    """To eat to when she gets full, Michaela needs 20 oranges. Cassandra needs twice as many oranges as Michaela to eat until she gets full. If they picked 90 oranges from the farm today, how many oranges would remain after they've both eaten until they were full?"""
    # Calculate the number of oranges needed by Cassandra
    cassandra_oranges = 2 * 20

    # Calculate the total number of oranges needed
    total_oranges = cassandra_oranges + 20

    # Calculate the number of oranges left after they've both eaten until they were full
    oranges_left = 90 - total_oranges

    # return the result
    result = oranges_left
    return result

print(solution())