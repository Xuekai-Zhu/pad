def solution():
    """Cassandra collected 5000 pennies for the charity drive. James collected 276 fewer pennies. How many pennies did they donate to charity?"""
    cassandra_pennies = 5000
    james_pennies = cassandra_pennies - 276
    total_pennies = cassandra_pennies + james_pennies
    result = total_pennies
    return result

print(solution())