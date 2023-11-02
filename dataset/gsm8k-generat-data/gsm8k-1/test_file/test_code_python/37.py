def solution():
    """The great dragon, Perg, sat high atop mount Farbo, breathing fire upon anything within a distance of 1000 feet. Polly could throw the gold javelin, the only known weapon that could sleigh the dragon, for a distance of 400 feet, well within the reach of the dragon's flames. But when Polly held the sapphire gemstone, she could throw the javelin three times farther than when not holding the gemstone. If holding the gemstone, how far outside of the reach of the dragon's flames could Polly stand and still hit the dragon with the gold javelin?"""
    dragon_distance = 1000
    javelin_distance = 400
    gemstone_multiplier = 3
    javelin_with_gemstone = javelin_distance * gemstone_multiplier
    safe_distance = dragon_distance + javelin_with_gemstone
    result = safe_distance
    return result

print(solution())