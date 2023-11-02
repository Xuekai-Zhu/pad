def solution():
    """To eat to when she gets full, Michaela needs 20 oranges. Cassandra needs twice as many oranges as Michaela to eat until she gets full. If they picked 90 oranges from the farm today, how many oranges would remain after they've both eaten until they were full?"""
    michaela_oranges = 20
    cassandra_oranges = 2 * michaela_oranges
    total_oranges_needed = michaela_oranges + cassandra_oranges
    remaining_oranges = 90 - total_oranges_needed
    result = remaining_oranges
    return result

print(solution())