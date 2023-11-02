def solution():
    days_left = 3
    goal = 1000
    earned_so_far = 300 + 40
    houses_visited = earned_so_far / 10 * 4  # Calculate the number of houses visited so far
    houses_left = (goal - earned_so_far) / 10 * 4  # Calculate the number of houses left to visit
    houses_per_day = houses_left / days_left  # Calculate the number of houses to visit per day
    result = houses_per_day
    return result

print(solution())