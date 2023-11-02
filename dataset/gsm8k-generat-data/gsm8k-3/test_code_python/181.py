def solution():
    """A certain tree was 100 meters tall at the end of 2017. It will grow 10% more than its previous height each year. How long has the tree grown from 2017 until the end of 2019?"""
    # Define the initial height of the tree and the growth rate
    initial_height = 100
    growth_rate = 0.1

    # Define the number of years passed
    years = 2

    # Calculate the height of the tree at the end of 2019
    final_height = initial_height * ((1 + growth_rate) ** years)

    # Calculate the difference in height from the initial height
    height_difference = final_height - initial_height

    # Round the height difference to the nearest whole number
    height_difference_rounded = round(height_difference)

    # Return the result
    result = height_difference_rounded
    return result

print(solution())