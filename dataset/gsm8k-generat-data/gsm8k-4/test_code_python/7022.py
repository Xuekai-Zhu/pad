def solution():
    """Suki bought 6.5 bags of coffee beans that each weighed 22 kilograms. Jimmy bought 4.5 bags of coffee beans that each weighed 18 kilograms. Suki and Jimmy combined their coffee beans and then repackaged them into 8-kilogram containers. How many containers did they use?"""
    # Define the weight of each bag of coffee beans
    suki_bag_weight = 22
    jimmy_bag_weight = 18

    # Calculate the total weight of Suki's and Jimmy's coffee beans
    total_weight = (suki_bag_weight * 6.5) + (jimmy_bag_weight * 4.5)

    # Calculate the number of 8-kilogram containers needed
    container_count = total_weight // 8

    # Return the result
    result = container_count
    return result

print(solution())