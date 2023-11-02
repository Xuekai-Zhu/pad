def solution():
    
    
    weekdays_rate = 420
    weekend_rate = 540
    days_weekdays = 2  
    days_weekend = 2  
    total_rent = (weekdays_rate * days_weekdays) + (weekend_rate * days_weekend)
    num_people = 6  
    rent_per_person = total_rent / num_people
    result = rent_per_person
    return result

print(solution())