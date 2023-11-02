def solution():
    """In one of the teacher's meetings, it was agreed that each class will contribute $90 for a school activity. The class of Miss Evans has $14 class funds and they decided to use it to lessen the contribution of each student. If the remaining amount will be divided among 19 students, how much will each student contribute?"""
    # Define the total contribution needed and the funds from Miss Evans' class
    total_contribution = 90 * 19
    miss_evans_funds = 14

    # Subtract Miss Evans' funds from the total contribution needed
    remaining_contribution = total_contribution - miss_evans_funds

    # Calculate the contribution of each student
    contribution_per_student = remaining_contribution / 19

    # Return the result
    result = contribution_per_student
    return result

print(solution())