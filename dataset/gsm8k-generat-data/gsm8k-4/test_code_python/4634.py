def solution():
    """Cassandra collected 5000 pennies for the charity drive. James collected 276 fewer pennies. How many pennies did they donate to charity?"""
    # Define the number of pennies collected by Cassandra
    cassandra_pennies = 5000

    # Calculate the number of pennies collected by James
    james_pennies = cassandra_pennies - 276

    # Calculate the total number of pennies donated
    total_pennies = cassandra_pennies + james_pennies

    # Return the result
    result = total_pennies
    return result

print(solution())