def solution():
    
    house_price = 100000
    down_payment = 0.2 * house_price
    remaining_balance = house_price - down_payment
    additional_payment = 0.3 * remaining_balance
    total_paid = down_payment + additional_payment
    still_owed = house_price - total_paid
    result = still_owed
    return result

print(solution())