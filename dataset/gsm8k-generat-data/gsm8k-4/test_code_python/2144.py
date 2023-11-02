def solution():
    """Sharon’s vacation rental has a Keurig coffee machine. She will be there for 40 days. She has 3 cups of coffee (3 coffee pods) every morning. Her coffee pods come 30 pods to a box for $8.00. How much will she spend on coffee to last her for the entire vacation?"""
    # Define the number of coffee pods Sharon needs per day
    coffee_pods_per_day = 3

    # Define the number of days Sharon will be on vacation
    vacation_days = 40

    # Calculate the total number of coffee pods Sharon needs
    total_coffee_pods = coffee_pods_per_day * vacation_days

    # Calculate the number of boxes of coffee pods Sharon needs to buy
    boxes_of_coffee_pods = total_coffee_pods // 30 + 1

    # Calculate the total cost of the coffee pods
    total_cost = boxes_of_coffee_pods * 8

    result = total_cost
    return result

print(solution())