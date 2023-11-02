def solution():
    """Marie ordered one chicken meal that costs $12, 5 packs of milk that costs $3 each, 4 apples that cost $1.50 each, and some boxes of pizza. Marie paid a total of $50. How many boxes of pizza did Marie order if each box costs $8.50?"""
    chicken_meal_cost = 12
    milk_packs_cost = 5 * 3
    apples_cost = 4 * 1.50
    total_items_cost = chicken_meal_cost + milk_packs_cost + apples_cost
    total_cost = 50
    pizza_cost = total_cost - total_items_cost
    boxes_of_pizza = pizza_cost / 8.50
    result = boxes_of_pizza
    return result

print(solution())