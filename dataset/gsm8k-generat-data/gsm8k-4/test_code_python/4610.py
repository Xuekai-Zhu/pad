def solution():
    """Camille goes to the Ice Cream Palace with her husband and two children. Each one orders a different ice cream. Camille orders a banana split, her husband orders a waffle bowl, her daughter orders a single cone, and her son orders a double cone. The cone has 1 scoop of ice cream, the banana split has 3 times as many scoops of ice cream as the cone and the waffle bowl has 1 more scoop than the banana split. How many scoops of ice cream did the ice cream man serve?"""
    # Define the number of scoops of ice cream in a cone
    cone_scoops = 1

    # Calculate the number of scoops in a banana split
    banana_scoops = cone_scoops * 3

    # Calculate the number of scoops in a waffle bowl
    waffle_scoops = banana_scoops + 1

    # Calculate the total number of scoops served by the ice cream man
    total_scoops = cone_scoops + banana_scoops + waffle_scoops + (2 * cone_scoops)

    # return the result
    result = total_scoops
    return result

print(solution())