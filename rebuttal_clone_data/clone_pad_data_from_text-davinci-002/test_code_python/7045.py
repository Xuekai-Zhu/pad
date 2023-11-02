def solution():
    hourly_rate = 5
    hours_vacuuming = 2
    hours_washing_dishes = 0.5
    hours_cleaning_bathroom = hours_vacuuming * 3
    total_hours = hours_vacuuming * 2 + hours_washing_dishes + hours_cleaning_bathroom
    total_earnings = hourly_rate * total_hours
    
    result = total_earnings
    
    return result

print(solution())