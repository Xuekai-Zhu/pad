def solution():
    # Convert 1 quart to ounces
    quart_to_ounces = 32

    # Define the size of the hot sauce container in ounces
    container_size = quart_to_ounces - 2

    # Calculate the number of servings in the container
    servings_in_container = container_size / 0.5

    # Calculate the number of days the container will last based on James' daily usage
    days_lasting = servings_in_container / 3
    result = days_lasting
    return result

print(solution())