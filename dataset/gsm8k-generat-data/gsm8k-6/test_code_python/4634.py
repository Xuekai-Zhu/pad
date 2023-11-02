def solution():
    cassandra_pennies = 5000  # number of pennies Cassandra collected
    james_pennies = cassandra_pennies - 276  # number of pennies James collected
    total_pennies = cassandra_pennies + james_pennies  # total number of pennies donated to charity
    result = total_pennies
    return result

print(solution())