def solution():
    """Julie orders $10 worth of food, Letitia orders $20 worth of food, and Anton orders $30 worth of food.
    How much should each pay in tips if they want to split a 20% tip for the whole meal evenly?"""
    total_bill = 10 + 20 + 30  # $60 for the whole meal
    tip_percent = 0.2
    tip_amount = total_bill * tip_percent
    total_with_tip = total_bill + tip_amount
    number_of_people = 3  # Julie, Letitia, and Anton
    per_person_cost = total_with_tip / number_of_people
    tip_per_person = tip_amount / number_of_people

    result = tip_per_person
    return result

print(solution())