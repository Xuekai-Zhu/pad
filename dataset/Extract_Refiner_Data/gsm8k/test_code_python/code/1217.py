def solution():
    
    # Define the number of meatballs needed
    meatballs_needed = 80

    # Calculate the number of pounds of ground beef used
    pounds_used = meatballs_needed / 16

    # Calculate the amount of secret seasoning needed
    seasoning_needed = pounds_used * 2

    # return the result
    result = seasoning_needed
    return result

print(solution())