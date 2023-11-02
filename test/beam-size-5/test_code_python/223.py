def solution():
    base_burrito = 6.50
    extra_meat = 2.00
    extra_cheese = 1.00
    avocado = 1.00
    sauces = 2.25
    meal_extra = 3.00
    gift_card = 5.00

    # Calculate the total cost of the burrito
    total_cost = base_burrito + extra_meat + extra_cheese + avocado + sauces

    # Add the extra meal and the gift card
    total_cost += meal_extra + gift_card

    # Calculate how much Chad still owes
    still_owes = base_burrito - total_cost
    result = still_owes
    return result

print(solution())