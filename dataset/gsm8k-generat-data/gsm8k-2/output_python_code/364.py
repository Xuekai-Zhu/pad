def solution():
    """In a race, there are eight runners. The first five runners finish the race in 8 hours, while the rest of the runners finish the race 2 hours later. Calculate the total time the eight runners took to finish the race."""
    first_five_time = 8
    last_three_time = 10
    total_time = (first_five_time * 5) + (last_three_time * 3)
    result = total_time
    return result

print(solution())