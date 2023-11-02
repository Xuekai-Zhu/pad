def solution():
    """Eden's mom is twice as old as Eden, who is twice as old as Devin. If Devin is 12 years old, what's the average age of the three?"""
    devin_age = 12
    eden_age = 2 * devin_age
    mom_age = 2 * eden_age
    avg_age = (devin_age + eden_age + mom_age) / 3
    result = avg_age
    return result

print(solution())