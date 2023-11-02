def solution():
    number_of_friends = 5
    commute_distance = 21
    commute_frequency = 5
    month_length = 4
    gas_price = 2.5
    mpg = 30
    gallons_per_month = (commute_distance * 2 * commute_frequency * month_length) / mpg
    total_monthly_gas_cost = gallons_per_month * gas_price
    contribution_per_friend = total_monthly_gas_cost / number_of_friends
    result = contribution_per_friend
    
    return result

print(solution())