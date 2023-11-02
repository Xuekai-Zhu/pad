def solution():
    """Christine and Rachel went strawberry picking. They want to make pies and need 3 pounds of strawberries per pie. Christine picked 10 pounds of strawberries and Rachel picked twice as much as Rachel. Together, how many pies can they make?"""
    pounds_per_pie = 3
    christine_picked = 10
    rachel_picked = christine_picked * 2
    total_picked = christine_picked + rachel_picked
    pies = total_picked // pounds_per_pie
    result = pies
    return result

print(solution())