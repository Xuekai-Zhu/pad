def solution():
    # Calculate the total time it takes to get from the top to the bottom of the garage
    total_time = 0
    for floor in range(12, 0, -1):
        if floor % 3 == 0:
            total_time += 120  # it takes 2 minutes to go through the gate
        total_time += 80  # it takes 80 seconds to travel 800 feet at 10 feet/second
    result = total_time
    return result

print(solution())