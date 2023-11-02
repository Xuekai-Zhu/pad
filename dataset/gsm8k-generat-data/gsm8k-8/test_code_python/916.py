def solution():
    # Calculate the age difference between Asaf and Alexander
    age_difference = 0.5 * 50
    
    # Calculate Alexander's age
    alexander_age = 140 - 50 - age_difference
    
    # Calculate the total number of pencils Asaf has
    total_pencils = (50 + 60) * 2
    
    # Calculate the total number of pencils they have together
    total_pencils_together = total_pencils + age_difference
    
    result = total_pencils_together
    return result

print(solution())