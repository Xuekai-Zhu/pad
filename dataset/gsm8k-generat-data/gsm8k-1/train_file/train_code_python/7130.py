def solution():
    """Donna worked 2 hours every morning walking dogs in her neighborhood for $10.00 an hour. 5 days a week, after school, she worked at a card shop for 2 hours and made $12.50 an hour. On the weekends, she usually made $10.00 an hour babysitting and was guaranteed 4 hours every Saturday from her neighbor. How much money did she make over 7 days?"""
    morning_hours = 2
    morning_rate = 10
    morning_pay = morning_hours * morning_rate * 5
    
    afternoon_hours = 2
    afternoon_rate = 12.5
    afternoon_pay = afternoon_hours * afternoon_rate * 5
    
    weekend_hours = 4
    weekend_rate = 10
    weekend_pay = weekend_hours * weekend_rate * 2
    
    total_pay = morning_pay + afternoon_pay + weekend_pay
    result = total_pay
    return result

print(solution())