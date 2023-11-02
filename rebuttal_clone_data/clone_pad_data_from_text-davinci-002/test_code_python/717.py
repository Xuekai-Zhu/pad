def solution():
    number_of_shots = 8
    ounces_per_shot = 1.5
    alcohol_percentage = 50
    total_alcohol = number_of_shots * ounces_per_shot * (alcohol_percentage / 100)
    result = total_alcohol 
    
    return result

print(solution())