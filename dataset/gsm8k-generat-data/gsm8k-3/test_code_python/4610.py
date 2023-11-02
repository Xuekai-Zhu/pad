def solution():
    """Camille goes to the Ice Cream Palace with her husband and two children. Each one orders a different ice cream. Camille orders a banana split, her husband orders a waffle bowl, her daughter orders a single cone, and her son orders a double cone. The cone has 1 scoop of ice cream, the banana split has 3 times as many scoops of ice cream as the cone and the waffle bowl has 1 more scoop than the banana split. How many scoops of ice cream did the ice cream man serve?"""
    # Define the number of scoops of ice cream in a cone, banana split, and waffle bowl
    CONE_SCOOPS = 1
    BANANA_SCOOPS = 3 * CONE_SCOOPS
    WAFFLE_SCOOPS = BANANA_SCOOPS + 1

    # Calculate the total number of scoops ordered
    total_scoops = CONE_SCOOPS + BANANA_SCOOPS + WAFFLE_SCOOPS + 2 * CONE_SCOOPS

    # Display the total number of scoops served
    result = total_scoops
    return result

print(solution())