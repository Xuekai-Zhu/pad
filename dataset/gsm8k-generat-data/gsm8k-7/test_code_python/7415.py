def solution():
    total_time = 38
    downstairs_time = x
    upstairs_time = 2x+5

    # Set up equation for total vacuuming time
    total_time = downstairs_time + upstairs_time

    # Solve for upstairs vacuuming time
    upstairs_time = total_time - downstairs_time
    upstairs_time = 2x+5
    x = (total_time - 5) / 3

    result = 2*x+5
    return result

print(solution())