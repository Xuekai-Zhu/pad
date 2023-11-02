def solution():
    """Lana and Mike are taking their dog and renting a cabin in the mountains for 2 weeks. The daily rate is $125.00 There is a $100.00 pet fee. There is also a 20% service/cleaning fee for the rental. They need to pay 50% of the entire bill as a security deposit. How much is their security deposit?"""
    daily_rate = 125
    pet_fee = 100
    service_fee_percent = 20
    rental_days = 14
    rental_cost = (daily_rate * rental_days) + pet_fee
    service_fee = rental_cost * (service_fee_percent / 100)
    total_cost = rental_cost + service_fee
    security_deposit = total_cost * 0.5
    result = security_deposit
    
    return result

print(solution())