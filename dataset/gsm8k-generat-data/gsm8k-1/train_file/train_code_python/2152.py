def solution():
    """Felicia is baking a cake. She needs 2 cups of flour, a cup of white sugar, a 1/4 cup of brown sugar, and a 1/2 cup of oil. Her only measuring scoop is 1/4 cup. How many times does she fill it to complete the measurements?"""
    flour = 2
    white_sugar = 1
    brown_sugar = 0.25
    oil = 0.5
    measuring_scoop = 0.25
    flour_scoops = flour / measuring_scoop
    white_sugar_scoops = white_sugar / measuring_scoop
    brown_sugar_scoops = brown_sugar / measuring_scoop
    oil_scoops = oil/ measuring_scoop
    total_scoops = flour_scoops + white_sugar_scoops + brown_sugar_scoops + oil_scoops
    result = total_scoops
    return result

print(solution())