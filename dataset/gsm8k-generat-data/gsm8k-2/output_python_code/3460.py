def solution():
    """In San Diego Zoo, the lion consumes 25 kilograms of meat, and the tiger consumes 20 kilograms of meat per day. If they have 90 kilograms of meat, how many days will the meats last?"""
    lion_meat_per_day = 25
    tiger_meat_per_day = 20
    total_meat = 90
    total_meat_per_day = lion_meat_per_day + tiger_meat_per_day
    days = total_meat / total_meat_per_day
    result = days
    return result

print(solution())