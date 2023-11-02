def solution():
    gladys_age = 30
    billy_age = gladys_age / 3
    lucas_age = (gladys_age / 2) - billy_age
  
    # Calculate Lucas' age three years from now
    lucas_age_in_3_years = lucas_age + 3
    result = lucas_age_in_3_years
    return result

print(solution())