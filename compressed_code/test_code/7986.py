def solution():
    
    brayan_coffee_per_hour = 4
    ivory_coffee_per_hour = brayan_coffee_per_hour / 2
    total_coffee_per_hour = brayan_coffee_per_hour + ivory_coffee_per_hour
    hours_coffee_was_consumed = 5
    total_coffee_consumed = total_coffee_per_hour * hours_coffee_was_consumed
    result = total_coffee_consumed
    return result

print(solution())