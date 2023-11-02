def solution():
    """There were 90 jellybeans in a jar. Samantha snuck 24 jellybeans out of the jar, without being seen. Shelby ate 12 jellybeans from the jar. Their mom, Shannon, refilled the jar with half as much as Samantha and Shelby took out. How many jellybeans are in the jar now?"""
    starting_jellybeans = 90
    samantha_taken = 24
    shelby_eaten = 12
    total_taken = samantha_taken + shelby_eaten
    refill_amount = total_taken / 2
    final_jellybeans = starting_jellybeans - total_taken + refill_amount
    result = final_jellybeans
    return result

print(solution())