def solution():
    """Tina's bag contains nine apples, 5 oranges, and 17 tangerines. If she took away 2 oranges and 10 tangerines, how many more tangerines than oranges would she have left?"""
    # Define the initial number of each fruit
    apples = 9
    oranges = 5
    tangerines = 17

    # Remove 2 oranges and 10 tangerines
    oranges -= 2
    tangerines -= 10

    # Calculate the difference between tangerines and oranges
    difference = tangerines - oranges

    # Display the result
    result = difference
    return result

print(solution())