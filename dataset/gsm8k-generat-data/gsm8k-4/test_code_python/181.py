def solution():
    """A certain tree was 100 meters tall at the end of 2017. It will grow 10% more than its previous height each year. How long has the tree grown from 2017 until the end of 2019?"""
    # Define the initial height of the tree and the growth rate
    height = 100
    growth_rate = 0.1

    # Calculate the height of the tree at the end of 2018
    height_2018 = height * (1 + growth_rate)

    # Calculate the height of the tree at the end of 2019
    height_2019 = height_2018 * (1 + growth_rate)

    # Calculate the total growth of the tree over the two years
    total_growth = height_2019 - height

    # Display the result
    result = round(total_growth, 2)
    return result

print(solution())