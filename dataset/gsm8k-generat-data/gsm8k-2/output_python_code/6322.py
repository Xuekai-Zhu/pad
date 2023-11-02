def solution():
    """There were 90 jellybeans in a jar. Samantha snuck 24 jellybeans out of the jar, without being seen. Shelby ate 12 jellybeans from the jar. Their mom, Shannon, refilled the jar with half as much as Samantha and Shelby took out. How many jellybeans are in the jar now?"""
    initial_count = 90
    samantha_took = 24
    shelby_ate = 12
    total_removed = samantha_took + shelby_ate
    refill_amount = total_removed / 2
    remaining_count = initial_count - total_removed + refill_amount
    result = remaining_count
    return result

print(solution())