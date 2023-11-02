def solution():
    """Axel has 50 silver pesos and 80 gold pesos. He visits her friend Anna who has twice as many silver pesos as he has and 40 more gold pesos. What's the total number of pesos they have together?"""
    axel_silver = 50
    axel_gold = 80
    anna_silver = axel_silver * 2
    anna_gold = axel_gold + 40
    total_silver = axel_silver + anna_silver
    total_gold = axel_gold + anna_gold
    total_pesos = total_silver + total_gold
    result = total_pesos
    return result

print(solution())