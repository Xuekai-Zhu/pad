def solution():
    """Mike wants to buy a new car. He has chosen a red car for $35000. To be able to pay this price, he needs to loan part of the money from the bank, at a rate of 15%. How much money in total will Mike need to pay for the car, if he has to take $20000 from the bank?"""
    car_price = 35000
    loan_amount = 20000
    loan_rate = 0.15
    loan_interest = loan_amount * loan_rate
    total_price = car_price + loan_interest
    result = total_price
    return result

print(solution())