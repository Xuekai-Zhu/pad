def solution():
    """Mason, Noah and Jacob want to have an eating contest but can't agree on what food to eat.
    Mason wants hot dogs, Noah insists on burgers, and Jacob thinks they should eat pies.
    They finally agree that everyone can eat whatever they want and they'll use the weight of the food to determine who wins.
    A hot dog weighs 2 ounces, a burger weighs 5 ounces, and a pie weighs 10 ounces.
    Jacob eats three fewer pies than Noah eats burgers.
    Mason eats 3 times as many hotdogs as the number of pies consumed by Jacob.
    If Noah ate 8 burgers, what is the total weight of the hotdogs that Mason ate?"""
    # Define the weight of each type of food
    HOTDOG_WEIGHT = 2
    BURGER_WEIGHT = 5
    PIE_WEIGHT = 10

    # Noah ate 8 burgers
    noah_burgers = 8

    # Jacob ate three fewer pies than Noah ate burgers
    jacob_pies = noah_burgers - 3

    # Mason ate 3 times the number of pies Jacob ate
    mason_hotdogs = jacob_pies * 3

    # Calculate the total weight of the hotdogs Mason ate
    total_hotdog_weight = mason_hotdogs * HOTDOG_WEIGHT

    # Display the total weight of the hotdogs Mason ate
    result = total_hotdog_weight
    return result

print(solution())