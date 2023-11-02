def solution():
    """Suki bought 6.5 bags of coffee beans that each weighed 22 kilograms. Jimmy bought 4.5 bags of coffee beans that each weighed 18 kilograms. Suki and Jimmy combined their coffee beans and then repackaged them into 8-kilogram containers. How many containers did they use?"""
    suki_bags = 6.5
    suki_weight = 22
    jimmy_bags = 4.5
    jimmy_weight = 18
    total_weight = (suki_bags * suki_weight) + (jimmy_bags * jimmy_weight)
    containers = total_weight / 8
    result = containers
    return result

print(solution())