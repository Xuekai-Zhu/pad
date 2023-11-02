def solution():
    # Calculate the number of paintings Marcus painted each day
    paintings_per_day = [2]  # Marcus paints 2 paintings on the first day
    for i in range(1, 5):
        paintings_per_day.append(2 * paintings_per_day[i-1])

    # Calculate the total number of paintings painted by Marcus
    total_paintings = sum(paintings_per_day)
    result = total_paintings
    return result

print(solution())