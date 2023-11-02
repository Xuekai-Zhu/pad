def solution():
    """Mario has 3 hibiscus plants in his garden. The first hibiscus plant has 2 flowers. The second hibiscus plant has twice as many flowers as the first hibiscus plant. The third hibiscus plant has four times as many flowers as the second hibiscus plant. How many total blossoms does Mario have?"""
    # Define the number of flowers on the first hibiscus plant
    hibiscus1 = 2

    # Define the number of flowers on the second hibiscus plant
    hibiscus2 = hibiscus1 * 2

    # Define the number of flowers on the third hibiscus plant
    hibiscus3 = hibiscus2 * 4

    # Calculate the total number of flowers
    total_flowers = hibiscus1 + hibiscus2 + hibiscus3

    # return the result
    result = total_flowers
    return result

print(solution())