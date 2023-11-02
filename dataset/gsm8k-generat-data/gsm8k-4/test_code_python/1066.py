def solution():
    """George and Amelia are picking oranges and apples at an orchard. George picks 45 oranges and 5 more apples than Amelia. Amelia picks 18 fewer oranges than George and 15 apples. How many fruits do they pick altogether?"""
    # Define the number of oranges and apples picked by George and Amelia
    george_oranges = 45
    george_apples = None
    amelia_oranges = None
    amelia_apples = None

    # Calculate the number of apples picked by George
    george_apples = george_oranges + 5

    # Calculate the number of oranges picked by Amelia
    amelia_oranges = george_oranges - 18

    # Calculate the number of apples picked by Amelia
    amelia_apples = george_apples - 15

    # Calculate the total number of fruits picked
    total_fruits = george_oranges + george_apples + amelia_oranges + amelia_apples

    # return the result
    result = total_fruits
    return result

print(solution())