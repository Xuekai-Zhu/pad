def solution():
    """Suki bought 6.5 bags of coffee beans that each weighed 22 kilograms. Jimmy bought 4.5 bags of coffee beans that each weighed 18 kilograms. Suki and Jimmy combined their coffee beans and then repackaged them into 8-kilogram containers. How many containers did they use?"""
    # Define the weight of a bag of coffee beans and the weight of a container
    BAG_WEIGHT = 22
    CONTAINER_WEIGHT = 8

    # Calculate the total weight of Suki's coffee beans
    suki_weight = 6.5 * BAG_WEIGHT

    # Calculate the total weight of Jimmy's coffee beans
    jimmy_weight = 4.5 * 18

    # Calculate the total weight of all the coffee beans
    total_weight = suki_weight + jimmy_weight

    # Calculate the number of containers needed
    containers_needed = total_weight // CONTAINER_WEIGHT

    # Display the number of containers needed
    result = containers_needed
    return result

print(solution())