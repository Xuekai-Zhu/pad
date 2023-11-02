def solution():
    """It was Trevor's job to collect fresh eggs from the family's 4 chickens every morning. He got 4 eggs from Gertrude and 3 eggs from Blanche. Nancy laid 2 eggs as did Martha. On the way, he dropped 2 eggs. How many eggs did Trevor have left?"""
    total_eggs = 4 + 3 + 2 + 2
    eggs_dropped = 2
    eggs_left = total_eggs - eggs_dropped
    result = eggs_left
    return result

print(solution())