def solution():
    
    salary_damages = 50000 * 30
    medical_damages = 200000
    punitive_damages = 3 * (salary_damages + medical_damages)
    total_damages = salary_damages + medical_damages + punitive_damages
    settlement = total_damages * 0.8
    result = settlement
    return result

print(solution())