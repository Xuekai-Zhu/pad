def solution():
    # Calculate the number of pies consumed by Jacob
    jacob_pies = noah_burgers - 3  # Jacob eats three fewer pies than Noah eats burgers

    # Calculate the number of hotdogs consumed by Mason
    mason_hotdogs = 3 * jacob_pies  # Mason eats 3 times as many hotdogs as the number of pies consumed by Jacob

    # Calculate the total weight of hotdogs consumed by Mason
    mason_hotdogs_weight = mason_hotdogs * 2  # A hotdog weighs 2 ounces

    result = mason_hotdogs_weight
    return result

print(solution())