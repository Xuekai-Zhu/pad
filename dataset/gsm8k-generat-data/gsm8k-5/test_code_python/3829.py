def solution():
    # Initial counts of fruits in Tina's bag
    apples = 9
    oranges = 5
    tangerines = 17

    # Remove 2 oranges and 10 tangerines
    oranges -= 2
    tangerines -= 10

    # Calculate the difference between tangerines and oranges
    difference = tangerines - oranges
    result = difference
    return result

print(solution())