def solution():
    """During 5 hours, a spider can catch 9 flies. How many flies would this spider catch in 30 hours if he would keep his efficiency?"""
    # Define the spider's efficiency in flies per hour
    efficiency = 9 / 5

    # Calculate the number of flies caught in 30 hours
    flies_caught = efficiency * 30

    # Return the result
    result = flies_caught
    return result

print(solution())