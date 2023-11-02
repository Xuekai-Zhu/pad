def solution():
    initial_oranges = 10
    added_oranges = 5
    total_oranges = initial_oranges + added_oranges

    # Calculate the total oranges needed for 2 weeks
    oranges_per_week = total_oranges * 2
    total_oranges += oranges_per_week * 2

    result = total_oranges
    return result

print(solution())