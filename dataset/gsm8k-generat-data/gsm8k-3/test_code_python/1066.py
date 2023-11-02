def solution():
    """George and Amelia are picking oranges and apples at an orchard. George picks 45 oranges and 5 more apples than Amelia. Amelia picks 18 fewer oranges than George and 15 apples. How many fruits do they pick altogether?"""
    # Define the number of fruits picked by George and Amelia
    george_oranges = 45
    george_apples = george_oranges + 5
    amelia_oranges = george_oranges - 18
    amelia_apples = 15

    # Calculate the total number of oranges and apples picked
    total_oranges = george_oranges + amelia_oranges
    total_apples = george_apples + amelia_apples

    # Calculate the total number of fruits picked
    total_fruits = total_oranges + total_apples

    # Display the total number of fruits picked
    result = total_fruits
    return result

print(solution())