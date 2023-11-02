def solution():
    """In San Diego Zoo, the lion consumes 25 kilograms of meat, and the tiger consumes 20 kilograms of meat per day. If they have 90 kilograms of meat, how many days will the meats last?"""
    lion_meat = 25
    tiger_meat = 20
    total_meat = 90
    daily_consumption = lion_meat + tiger_meat
    days_last = total_meat / daily_consumption
    result = days_last
    return result

print(solution())