def solution():
    """It was Trevor's job to collect fresh eggs from the family's 4 chickens every morning. He got 4 eggs from Gertrude and 3 eggs from Blanche. Nancy laid 2 eggs as did Martha. On the way, he dropped 2 eggs. How many eggs did Trevor have left?"""
    eggs_from_gertrude = 4
    eggs_from_blanche = 3
    eggs_from_nancy = 2
    eggs_from_martha = 2
    eggs_dropped = 2
    total_eggs = eggs_from_gertrude + eggs_from_blanche + eggs_from_nancy + eggs_from_martha - eggs_dropped
    result = total_eggs
    return result

print(solution())