def solution():
    """Christine and Rachel went strawberry picking. They want to make pies and need 3 pounds of strawberries per pie. Christine picked 10 pounds of strawberries and Rachel picked twice as much as Rachel. Together, how many pies can they make?"""
    pies_per_pound = 1/3
    christine_strawberries = 10
    rachel_strawberries = 2 * christine_strawberries
    total_strawberries = christine_strawberries + rachel_strawberries
    total_pies = total_strawberries * pies_per_pound
    result = total_pies
    return result

print(solution())