def solution():
    """Mason, Noah and Jacob want to have an eating contest but can't agree on what food to eat. Mason wants hot dogs, Noah insists on burgers, and Jacob thinks they should eat pies. They finally agree that everyone can eat whatever they want and they'll use the weight of the food to determine who wins. A hot dog weighs 2 ounces, a burger weighs 5 ounces, and a pie weighs 10 ounces. Jacob eats three fewer pies than Noah eats burgers. Mason eats 3 times as many hotdogs as the number of pies consumed by Jacob. If Noah ate 8 burgers, what is the total weight of the hotdogs that Mason ate?"""
    # Define the weight of each food item
    HOTDOG_WEIGHT = 2
    BURGER_WEIGHT = 5
    PIE_WEIGHT = 10

    # Noah eats 8 burgers
    burgers_noah = 8

    # Jacob eats three fewer pies than Noah eats burgers
    pies_jacob = burgers_noah - 3

    # Mason eats 3 times as many hotdogs as the number of pies consumed by Jacob
    hotdogs_mason = 3 * pies_jacob

    # Total weight of hotdogs that Mason ate
    weight_hotdogs_mason = hotdogs_mason * HOTDOG_WEIGHT

    result = weight_hotdogs_mason
    return result

print(solution())