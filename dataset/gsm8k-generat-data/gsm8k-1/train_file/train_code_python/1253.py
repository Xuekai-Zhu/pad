def solution():
    """Emilia needs 42 cartons of berries to make a berry cobbler. She already has 2 cartons of strawberries and 7 cartons of blueberries in her cupboard. She decides to go to the supermarket to get more cartons. How many more cartons of berries should Emilia buy?"""
    total_cartons_needed = 42
    strawberries_in_cupboard = 2
    blueberries_in_cupboard = 7
    cartons_in_cupboard = strawberries_in_cupboard + blueberries_in_cupboard
    cartons_to_buy = total_cartons_needed - cartons_in_cupboard
    result = cartons_to_buy
    return result

print(solution())