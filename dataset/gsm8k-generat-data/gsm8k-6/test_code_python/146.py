def solution():
    # Find the time taken by Cory and Blake to clean their rooms
    cory_time = 22 + 3
    blake_time = cory_time - 4

    # Calculate the total time taken by all three to clean their rooms twice a week
    total_time = 2 * (22 + cory_time + blake_time)

    result = total_time
    return result

print(solution())