def solution():
    # Find Mandy's current age
    current_age = 6 + 2 * 6 + 8  # Mandy was twice her age at 12, and then 8 years later, she was 20.
    
    # Find the length of the books Mandy was reading at age 12
    length_at_12 = 8 * 5  # Mandy's books were 5 times longer
    
    # Find the length of the books Mandy was reading at age 20
    length_at_20 = length_at_12 * 3  # Mandy's books were 3 times longer than at age 12
    
    # Find the length of the books Mandy reads currently
    current_length = length_at_20 * 4  # Mandy's current books are 4 times longer than at age 20
    
    result = current_length
    return result

print(solution())