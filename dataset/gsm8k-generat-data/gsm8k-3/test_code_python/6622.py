def solution():
    """Louis has 5 oranges and 3 apples. Samantha has 8 oranges and 7 apples. If Marley has twice as many oranges as Louis and three times as many apples as Samantha, how many fruits in total does Marley have?"""
    # Define the number of oranges and apples Louis and Samantha have
    louis_oranges = 5
    louis_apples = 3
    samantha_oranges = 8
    samantha_apples = 7

    # Calculate the number of oranges and apples Marley has
    marley_oranges = 2 * louis_oranges
    marley_apples = 3 * samantha_apples

    # Calculate the total number of fruits Marley has
    total_fruits = marley_oranges + marley_apples

    # Display the total number of fruits Marley has
    result = total_fruits
    return result

print(solution())