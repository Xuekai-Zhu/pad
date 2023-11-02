def solution():
    """Lana and Mike are taking their dog and renting a cabin in the mountains for 2 weeks. The daily rate is $125.00 There is a $100.00 pet fee. There is also a 20% service/cleaning fee for the rental. They need to pay 50% of the entire bill as a security deposit. How much is their security deposit?"""
    daily_rate = 125.00
    pet_fee = 100.00
    rental_duration = 14
    sub_total = (daily_rate * rental_duration) + pet_fee
    service_fee = 0.2 * sub_total
    total_bill = sub_total + service_fee
    security_deposit = 0.5 * total_bill
    result = security_deposit
    return result

print(solution())