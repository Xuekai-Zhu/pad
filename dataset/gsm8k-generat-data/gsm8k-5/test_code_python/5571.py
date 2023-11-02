def solution():
    hotdog_weight = 2  # ounces
    burger_weight = 5  # ounces
    pie_weight = 10  # ounces

    # Jacob ate 3 fewer pies than Noah ate burgers
    jacob_pies = 8 - 3
    # Mason ate 3 times as many hotdogs as the number of pies consumed by Jacob
    mason_hotdogs = 3 * jacob_pies

    # Calculate the total weight of hotdogs that Mason ate
    total_hotdog_weight = mason_hotdogs * hotdog_weight
    result = total_hotdog_weight
    return result

print(solution())