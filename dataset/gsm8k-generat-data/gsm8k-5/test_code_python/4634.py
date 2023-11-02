def solution():
    cassandra_pennies = 5000  # Cassandra collected 5000 pennies
    james_pennies = cassandra_pennies - 276  # James collected 276 fewer pennies

    # Calculate the total number of pennies donated by Cassandra and James
    total_pennies = cassandra_pennies + james_pennies

    result = total_pennies
    return result

print(solution())