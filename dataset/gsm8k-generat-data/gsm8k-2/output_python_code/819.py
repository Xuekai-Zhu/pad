def solution():
    """James goes out to eat. He orders a steak and egg meal for $16. He is with his friend, who orders chicken fried steak for $14. His friend pays for half the bill and James pays the tip along with his half of the bill. They tip 20%. How much did James pay?"""
    james_meal = 16
    friend_meal = 14
    total_bill = james_meal + friend_meal
    half_bill = total_bill / 2
    tip = 0.2 * total_bill
    james_payment = half_bill + tip
    result = james_payment
    return result

print(solution())