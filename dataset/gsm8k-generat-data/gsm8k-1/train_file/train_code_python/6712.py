def solution():
    """Charlotte is making a pie. She can't decide if she will make cherry or blueberry. So she decides to make whichever pie is cheapest. Both pies will need $2 for flour, $1 for sugar and $1.5 for eggs and butter to make the crust. The blueberry pie needs 3 pounds of blueberries. The blueberries come in 8 oz containers for $2.25. For the cherry pie, she needs 4 pounds and they come in a four-pound bag for $14. What is the total price to make the cheapest pie?"""
    flour_cost = 2
    sugar_cost = 1
    crust_cost = 1.5
    blueberries_weight = 3
    blueberries_container_cost = 2.25
    cherries_weight = 4
    cherries_bag_cost = 14
    
    blueberries_cost = (blueberries_container_cost / 0.5) * blueberries_weight
    cherry_cost = cherries_bag_cost / cherries_weight
    
    if blueberries_cost <= cherry_cost:
        total_cost = flour_cost + sugar_cost + crust_cost + blueberries_cost
    else:
        total_cost = flour_cost + sugar_cost + crust_cost + cherry_cost
        
    result = total_cost
    return result

print(solution())