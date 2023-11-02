def solution():
    num_apples = 9
    num_oranges = 5
    num_tangerines = 17

    # Take away 2 oranges and 10 tangerines
    num_oranges -= 2
    num_tangerines -= 10

    # Calculate the difference between the number of tangerines and oranges
    diff = num_tangerines - num_oranges
    result = diff
    return result

print(solution())