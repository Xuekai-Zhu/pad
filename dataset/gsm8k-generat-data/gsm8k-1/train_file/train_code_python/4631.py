def solution():
    """Julie, Letitia and Anton decided to have dinner together at a nearby restaurant.
    Julie orders $10 worth of food, Letitia orders $20 worth of food, and Anton orders $30 worth of food.
    How much should each pay in tips if they want to split a 20% tip for the whole meal evenly?"""
    
    total_bill = 10 + 20 + 30
    tip_percent = 20
    tip_amount = total_bill * (tip_percent/100)
    total_with_tip = total_bill + tip_amount
    num_people = 3
    tip_per_person = tip_amount/num_people
    result = tip_per_person
    return result

print(solution())