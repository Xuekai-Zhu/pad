def solution():
    """Dream's car consumes 4 gallons of gas per mile. 
    If she drives 400 miles today and 200 more miles tomorrow than today, 
    how many gallons of gas will the car consume?"""
    gas_per_mile = 4
    today_miles = 400
    tomorrow_miles = today_miles + 200
    total_miles = today_miles + tomorrow_miles
    gas_consumed = gas_per_mile * total_miles
    result = gas_consumed
    return result

print(solution())