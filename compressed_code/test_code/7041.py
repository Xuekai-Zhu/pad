def solution():
    
    michaela_oranges = 20
    cassandra_oranges = michaela_oranges * 2
    total_oranges = 90
    eaten_oranges = michaela_oranges + cassandra_oranges
    remaining_oranges = total_oranges - eaten_oranges
    result = remaining_oranges
    return result

print(solution())