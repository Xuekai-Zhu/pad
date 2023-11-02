def solution():
    # Number of oranges picked on Monday
    monday_oranges = 100

    # Number of oranges picked on Tuesday (three times as many as Monday)
    tuesday_oranges = 3 * monday_oranges

    # Number of oranges picked on Wednesday
    wednesday_oranges = 70

    # Total number of oranges picked
    total_oranges = monday_oranges + tuesday_oranges + wednesday_oranges
    result = total_oranges
    return result

print(solution())