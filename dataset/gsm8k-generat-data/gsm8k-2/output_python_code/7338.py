def solution():
    """Brooke is milking cows and then selling the milk at the market for $3 a gallon. Whatever milk doesn't sell, she turns into butter. One gallon of milk equals 2 sticks of butter. She then sells the butter for $1.5 a stick. She has 12 cows. Each cow produces 4 gallons of milk. She has 6 customers, each of whom wants 6 gallons of milk. How much money does she earn if she sells all her milk and butter?"""
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