def solution():
    total_miles = 70
    dog1_miles = 2 * 7 # 2 miles a day for 7 days
    dog2_miles = total_miles - dog1_miles
    num_days = 7
    dog2_avg_miles = dog2_miles / (num_days)
    result = dog2_avg_miles
    return result

print(solution())