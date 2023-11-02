def solution():
    """To eat to when she gets full, Michaela needs 20 oranges. Cassandra needs twice as many oranges as Michaela to eat until she gets full. 
    If they picked 90 oranges from the farm today, how many oranges would remain after they've both eaten until they were full?"""
    michaela_oranges = 20
    cassandra_oranges = michaela_oranges * 2
    total_oranges = 90
    eaten_oranges = michaela_oranges + cassandra_oranges
    remaining_oranges = total_oranges - eaten_oranges
    result = remaining_oranges
    return result

print(solution())