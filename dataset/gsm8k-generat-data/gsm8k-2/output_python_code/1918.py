def solution():
    """Roger bought a house for $100,000. He was able to pay 20% down, and his parents paid off an additional 30% of the remaining balance. How much money does Roger still owe on his house?"""
    house_price = 100000
    down_payment = 0.2 * house_price
    remaining_balance = house_price - down_payment
    additional_payment = 0.3 * remaining_balance
    total_paid = down_payment + additional_payment
    still_owed = house_price - total_paid
    result = still_owed
    return result

print(solution())