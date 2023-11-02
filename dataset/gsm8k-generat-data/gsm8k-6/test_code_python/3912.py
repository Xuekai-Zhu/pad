def solution():
    # Calculate the total amount paid over 5 years
    total_paid = 250 * 12 * 5  # monthly payment multiplied by 12 months per year for 5 years
    price_of_car = total_paid + 5000  # total paid plus down payment equals price of car
    result = price_of_car
    return result

print(solution())