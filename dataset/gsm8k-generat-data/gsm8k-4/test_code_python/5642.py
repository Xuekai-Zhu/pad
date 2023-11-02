def solution():
    """Christine and Rachel went strawberry picking. They want to make pies and need 3 pounds of strawberries per pie. Christine picked 10 pounds of strawberries and Rachel picked twice as much as Rachel. Together, how many pies can they make?"""
    # Define the amount of strawberries picked by Christine and Rachel
    christine_strawberries = 10
    rachel_strawberries = 20

    # Calculate the total amount of strawberries picked
    total_strawberries = christine_strawberries + rachel_strawberries

    # Calculate the number of pies that can be made
    pies = total_strawberries // 3

    result = pies
    return result

print(solution())