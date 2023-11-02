def solution():
    """Emilia needs 42 cartons of berries to make a berry cobbler. She already has 2 cartons of strawberries and 7 cartons of blueberries in her cupboard. She decides to go to the supermarket to get more cartons. How many more cartons of berries should Emilia buy?"""
    total_cartons = 42
    strawberries = 2
    blueberries = 7
    current_cartons = strawberries + blueberries
    remaining_cartons = total_cartons - current_cartons
    result = remaining_cartons
    return result

print(solution())