def solution():
    # Define the weight of each type of food
    hotdog_weight = 2
    burger_weight = 5
    pie_weight = 10

    # Calculate the number of pies Jacob eats based on Noah's burgers
    jacob_pies = 8 - 3
    
    # Calculate the number of hotdogs Mason eats based on Jacob's pies
    mason_hotdogs = 3 * jacob_pies

    # Calculate the total weight of hotdogs Mason eats
    total_hotdog_weight = mason_hotdogs * hotdog_weight
    result = total_hotdog_weight
    return result

print(solution())