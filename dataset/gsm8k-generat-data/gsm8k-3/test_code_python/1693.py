def solution():
    """Eden's mom is twice as old as Eden, who is twice as old as Devin. If Devin is 12 years old, what's the average age of the three?"""
    # Calculate Eden's age
    eden_age = 2 * 12

    # Calculate Eden's mom's age
    mom_age = 2 * eden_age

    # Calculate the total age of the three
    total_age = mom_age + eden_age + 12

    # Calculate the average age
    average_age = total_age / 3

    # Display the average age
    result = average_age
    return result

print(solution())