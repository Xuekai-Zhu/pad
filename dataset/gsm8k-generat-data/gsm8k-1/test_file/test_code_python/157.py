def solution():
    """Anakin and Locsin went to the beach today. Anakin caught 10 starfish, 6 sea horses, and 3 clownfish. While Locsin caught 5 fewer starfish than Anakin, 3 fewer sea horses than Anakin, and 2 more clownfish than Anakin. How many fish were they able to catch?"""
    anakin_starfish = 10
    anakin_seahorses = 6
    anakin_clownfish = 3
    
    locsin_starfish = anakin_starfish - 5
    locsin_seahorses = anakin_seahorses - 3
    locsin_clownfish = anakin_clownfish + 2
    
    total_fish = anakin_starfish + anakin_seahorses + anakin_clownfish + locsin_starfish + locsin_seahorses + locsin_clownfish
    
    result = total_fish
    return result

print(solution())