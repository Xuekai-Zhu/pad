def solution():
    """Cassandra collected 5000 pennies for the charity drive. James collected 276 fewer pennies. How many pennies did they donate to charity?"""
    # Define the number of pennies Cassandra collected
    cassandra_pennies = 5000

    # Calculate the number of pennies James collected
    james_pennies = cassandra_pennies - 276

    # Calculate the total number of pennies donated
    total_pennies = cassandra_pennies + james_pennies

    # Display the total number of pennies donated
    result = total_pennies
    return result

print(solution())