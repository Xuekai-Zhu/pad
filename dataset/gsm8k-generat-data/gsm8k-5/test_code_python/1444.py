def solution():
    emily_credits = 20  # Emily has 20 high school credits
    spencer_credits = emily_credits // 2  # Spencer has half as many credits as Emily
    aria_credits = 2 * emily_credits  # Aria has twice as many credits as Emily
    total_credits = emily_credits + spencer_credits + aria_credits  # Total number of credits of the three
    twice_total_credits = 2 * total_credits  # Twice the total number of credits
    result = twice_total_credits
    return result

print(solution())