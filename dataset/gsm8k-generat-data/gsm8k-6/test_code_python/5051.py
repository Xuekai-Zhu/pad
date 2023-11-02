def solution():
    # Calculate the total number of steps Eliana walked during the three days
    total_steps = 200 + 300 + 2*(200 + 300) + 100  # first day: 200 steps + 300 steps = 500; second day: 2*(200 + 300) = 1000; third day: additional 100 steps
    result = total_steps
    return result

print(solution())