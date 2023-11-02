def solution():
    days_per_week = 5
    string_cheeses_needed_per_day = 3
    string_cheeses_per_package = 30
    number_of_weeks = 4
    total_number_of_days = days_per_week * number_of_weeks
    total_number_of_string_cheeses_needed = total_number_of_days * string_cheeses_needed_per_day
    total_number_of_packages_needed = total_number_of_string_cheeses_needed / string_cheeses_per_package
    result = total_number_of_packages_needed
    
    return result

print(solution())