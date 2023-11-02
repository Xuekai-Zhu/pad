def solution():
    """There were 10 apples and 5 oranges in the basket. If Emily adds 5 more oranges to the basket, what percentage of the fruit in the basket would be apples?"""
    
    # Define the initial number of apples and oranges
    apples = 10
    oranges = 5

    # Add 5 more oranges
    oranges += 5

    # Calculate the total number of fruits
    total_fruits = apples + oranges

    # Calculate the percentage of apples in the basket
    apple_percentage = (apples / total_fruits) * 100

    result = apple_percentage
    return result

print(solution())