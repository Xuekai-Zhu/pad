def solution():
    """Charlotte is making a pie. She can't decide if she will make cherry or blueberry. So she decides to make whichever pie is cheapest. Both pies will need $2 for flour, $1 for sugar and $1.5 for eggs and butter to make the crust. The blueberry pie needs 3 pounds of blueberries. The blueberries come in 8 oz containers for $2.25. For the cherry pie, she needs 4 pounds and they come in a four-pound bag for $14. What is the total price to make the cheapest pie?"""
    crust_cost = 2 + 1 + 1.5
    blueberry_cost = crust_cost
    blueberry_cost += (3 * 16 / 8) * (2.25 / 2)
    cherry_cost = crust_cost
    cherry_cost += (14 / 4) * 4
    if blueberry_cost < cherry_cost:
        result = blueberry_cost
    else:
        result = cherry_cost
    return result

print(solution())