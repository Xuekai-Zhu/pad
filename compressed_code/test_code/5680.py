def solution():
    
    milk_price = 3
    butter_price = 1.5
    num_cows = 12
    gallons_per_cow = 4
    gallons_for_customers = 6 * 6
    total_milk = num_cows * gallons_per_cow
    unsold_milk = total_milk - gallons_for_customers
    total_butter = unsold_milk * 2
    milk_earnings = gallons_for_customers * milk_price
    butter_earnings = total_butter * butter_price
    total_earnings = milk_earnings + butter_earnings
    result = total_earnings
    return result

print(solution())