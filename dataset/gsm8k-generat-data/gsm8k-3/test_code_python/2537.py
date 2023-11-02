def solution():
    """James buys a jar of hot sauce. Each serving is .5 ounces. He uses 3 servings every day. if the container is 2 ounces less than 1 quart how many days will it last?"""
    # Convert 1 quart to ounces
    quart_to_oz = 32

    # Define the size of the jar of hot sauce in ounces
    jar_size = quart_to_oz - 2

    # Calculate the number of servings in the jar
    num_servings = jar_size / 0.5

    # Calculate the number of days the jar will last
    num_days = num_servings / 3

    # Display the number of days the jar will last
    result = num_days
    return result

print(solution())