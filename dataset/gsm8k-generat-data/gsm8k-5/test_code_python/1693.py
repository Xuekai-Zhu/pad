def solution():
    devin_age = 12  # Devin is 12 years old
    eden_age = devin_age * 2  # Eden is twice as old as Devin
    mom_age = eden_age * 2  # Eden's mom is twice as old as Eden

    # Calculate the average age of the three
    average_age = (devin_age + eden_age + mom_age) / 3
    result = average_age
    return result

print(solution())