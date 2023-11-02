def solution():
    oranges_on_monday = 100
    oranges_on_tuesday = 3 * oranges_on_monday
    oranges_on_wednesday = 70

    # Calculate the total number of oranges picked over three days
    total_oranges_picked = oranges_on_monday + oranges_on_tuesday + oranges_on_wednesday
    result = total_oranges_picked
    return result

print(solution())