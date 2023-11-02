def solution():
    """Smaug the dragon hoards 100 gold coins, 60 silver coins, and 33 copper coins. If each silver coin is worth 8 copper coins, and each gold coin is worth 3 silver coins, what is the total value of Smaug's hoard expressed as a number of copper coins?"""
    gold_value = 3 * 8  # Each gold coin is worth 24 copper coins
    silver_value = 8  # Each silver coin is worth 8 copper coins
    total_copper = (100 * gold_value) + (60 * silver_value) + 33
    result = total_copper
    return result

print(solution())