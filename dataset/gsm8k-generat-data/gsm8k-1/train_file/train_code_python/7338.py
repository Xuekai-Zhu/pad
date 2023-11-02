def solution():
    """Brooke is milking cows and then selling the milk at the market for $3 a gallon. Whatever milk doesn't sell, she turns into butter. One gallon of milk equals 2 sticks of butter. She then sells the butter for $1.5 a stick. She has 12 cows. Each cow produces 4 gallons of milk. She has 6 customers, each of whom wants 6 gallons of milk. How much money does she earn if she sells all her milk and butter?"""
    num_cows = 12
    gallons_per_cow = 4
    total_gallons = num_cows * gallons_per_cow
    num_customers = 6
    gallons_per_customer = 6
    total_gallons_sold = num_customers * gallons_per_customer
    total_gallons_unsold = total_gallons - total_gallons_sold
    # Calculate the total amount earned from selling milk
    milk_price_per_gallon = 3
    total_earned_from_milk = total_gallons_sold * milk_price_per_gallon
    # Calculate the total amount earned from selling butter
    butter_per_gallon = 2
    total_butter_produced = total_gallons_unsold * butter_per_gallon
    butter_price_per_stick = 1.5
    total_earned_from_butter = total_butter_produced * butter_price_per_stick
    # Calculate the total earnings
    total_earnings = total_earned_from_milk + total_earned_from_butter
    result = total_earnings
    return result

print(solution())