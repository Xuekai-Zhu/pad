def solution():
    # Calculate the total amount needed from Miss Evans' class
    total_amount = 90 * 19
    
    # Subtract the $14 class funds from the total amount needed
    remaining_amount = total_amount - 14
    
    # Divide the remaining amount equally among the 19 students
    contribution_per_student = remaining_amount / 19
    
    result = contribution_per_student
    return result

print(solution())