def solution():
    """Mason, Noah and Jacob want to have an eating contest but can't agree on what food to eat. Mason wants hot dogs, Noah insists on burgers, and Jacob thinks they should eat pies. They finally agree that everyone can eat whatever they want and they'll use the weight of the food to determine who wins. A hot dog weighs 2 ounces, a burger weighs 5 ounces, and a pie weighs 10 ounces. Jacob eats three fewer pies than Noah eats burgers. Mason eats 3 times as many hotdogs as the number of pies consumed by Jacob. If Noah ate 8 burgers, what is the total weight of the hotdogs that Mason ate?"""
    hotdog_weight = 2
    burger_weight = 5
    pie_weight = 10
    noah_burgers = 8
    jacob_pies = noah_burgers - 3
    mason_hotdogs = jacob_pies * 3
    mason_weight = mason_hotdogs * hotdog_weight
    result = mason_weight
    return result

print(solution())