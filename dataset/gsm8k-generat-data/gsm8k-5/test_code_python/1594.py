def solution():
    michaela_oranges = 20  # Michaela needs 20 oranges to eat until she gets full
    cassandra_oranges = 2 * michaela_oranges  # Cassandra needs twice as many oranges as Michaela to eat until she gets full
    total_oranges_needed = michaela_oranges + cassandra_oranges  # Total oranges needed by both of them

    oranges_picked = 90  # They picked 90 oranges from the farm

    # Calculate the remaining oranges after they both eat until they were full
    remaining_oranges = oranges_picked - total_oranges_needed
    result = remaining_oranges
    return result

print(solution())