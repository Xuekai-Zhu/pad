def solution():
    """Joe's bag of Halloween candy has 25 chocolate bars and 80 candied apples. Each chocolate bar weighs twice as much as each candied apple. If each chocolate bar weighs 40g, how much does Joe's bag of candy weigh, in grams?"""
    chocolate_bars = 25
    candied_apples = 80
    chocolate_weight = 40
    apple_weight = chocolate_weight / 2
    total_weight = chocolate_bars * chocolate_weight + candied_apples * apple_weight
    result = total_weight
    return result

print(solution())