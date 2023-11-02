def solution():
    """There were 10 apples and 5 oranges in the basket. If Emily adds 5 more oranges to the basket, what percentage of the fruit in the basket would be apples?"""
    # Define the starting number of apples and oranges
    apples = 10
    oranges = 5

    # Add 5 more oranges to the basket
    oranges += 5

    # Calculate the total number of fruits in the basket
    total_fruits = apples + oranges

    # Calculate the percentage of fruits that are apples
    apple_percentage = (apples / total_fruits) * 100

    # Display the percentage of fruits that are apples
    result = apple_percentage
    return result

print(solution())