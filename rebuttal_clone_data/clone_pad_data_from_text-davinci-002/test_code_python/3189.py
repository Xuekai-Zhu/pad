def solution():
    chickens_bought = 4
    chickens_after_two_years = 8 * chickens_bought
    eggs_laid_per_chicken = 6
    eggs_collected_per_week = eggs_laid_per_chicken * chickens_after_two_years
    result = eggs_collected_per_week
    
    return result

print(solution())