def solution():
    michaela_oranges = 20
    cassandra_oranges = michaela_oranges * 2
    total_oranges = 90

    # Calculate the total number of oranges they will eat combined
    total_eaten = michaela_oranges + cassandra_oranges

    # Calculate the number of oranges remaining
    oranges_remaining = total_oranges - total_eaten
    result = oranges_remaining
    return result

print(solution())