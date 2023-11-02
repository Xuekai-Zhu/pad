def solution():
    """The sum of Cooper’s, Dante’s, and Maria’s ages is 31. Dante is twice as old as Cooper. Maria is one year older than Dante. How old is Cooper?"""
    # Define the age of Cooper as x
    x = 0

    # Define the age of Dante as 2x
    dante_age = 2 * x

    # Define the age of Maria as 1 year older than Dante
    maria_age = dante_age + 1

    # Calculate the sum of all the ages
    total_age = x + dante_age + maria_age

    # Use the equation total_age = 31 to solve for x
    x = (31 - maria_age - dante_age) / 3

    # Round the age of Cooper to the nearest whole number
    cooper_age = round(x)

    # Display the age of Cooper
    result = cooper_age
    return result

print(solution())