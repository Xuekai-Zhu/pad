def solution():
    """Eden's mom is twice as old as Eden, who is twice as old as Devin. If Devin is 12 years old, what's the average age of the three?"""
    # Calculate Devin's age
    devin_age = 12

    # Calculate Eden's age
    eden_age = devin_age * 2

    # Calculate Eden's mom's age
    mom_age = eden_age * 2

    # Calculate the average age of the three
    avg_age = (devin_age + eden_age + mom_age) / 3

    result = avg_age
    return result

print(solution())