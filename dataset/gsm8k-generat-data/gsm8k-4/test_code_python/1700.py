def solution():
    """Mike wants to buy a new car. He has chosen a red car for $35000. To be able to pay this price, he needs to loan part of the money from the bank, at a rate of 15%. How much money in total will Mike need to pay for the car, if he has to take $20000 from the bank?"""
    # Define the price of the car and the amount borrowed
    car_price = 35000
    borrowed_amount = 20000

    # Calculate the interest on the loan
    loan_interest = borrowed_amount * 0.15

    # Calculate the total amount to be paid for the car
    total_amount = car_price + loan_interest

    # return the result
    result = total_amount
    return result

print(solution())