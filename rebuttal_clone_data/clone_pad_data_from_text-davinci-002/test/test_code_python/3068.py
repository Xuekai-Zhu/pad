def solution():
    chickens_added_annually = 150
    current_chicken_number = 550
    years = 9
    chickens_in_nine_years = current_chicken_number + (chickens_added_annually * years)
    result = chickens_in_nine_years
    return result

print(solution())