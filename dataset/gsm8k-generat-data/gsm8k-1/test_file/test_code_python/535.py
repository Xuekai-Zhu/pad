def solution():
    """My wife wants to evenly split the check but wants me to pay an additional 20% tip on our $50 dinner bill. How much did I end up paying?"""
    dinner_bill = 50
    tip_percent = 20
    tip_amount = dinner_bill * (tip_percent / 100)
    total_bill = dinner_bill + tip_amount
    amount_per_person = total_bill / 2
    result = amount_per_person
    return result

print(solution())