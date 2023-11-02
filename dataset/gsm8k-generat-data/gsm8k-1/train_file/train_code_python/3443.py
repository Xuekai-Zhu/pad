def solution():
    """Josie's mom gave her a $20 bill and asked her to go to the store for a few items. The list included a carton of milk for $4.00, a loaf of bread for $3.50, a box of laundry detergent for $10.25 and 2 pounds of bananas that were $0.75 per pound. Her mom also gave her a coupon for $1.25 off of the laundry detergent. At checkout, the clerk told her the milk was 1/2 off today. How much money did Josie have left over after she bought all of the groceries?"""
    starting_money = 20
    milk_cost = 4
    bread_cost = 3.5
    detergent_cost = 10.25
    banana_cost = 0.75
    banana_weight = 2
    detergent_coupon = 1.25
    milk_discount = milk_cost / 2
    total_cost = milk_discount + bread_cost + detergent_cost - detergent_coupon + (banana_cost * banana_weight)
    leftover_money = starting_money - total_cost
    result = leftover_money
    return result

print(solution())