def solution():
    
    james_meal = 16
    friend_meal = 14
    total_bill = james_meal + friend_meal
    half_bill = total_bill / 2
    tip = 0.2 * total_bill
    james_payment = half_bill + tip
    result = james_payment
    return result

print(solution())