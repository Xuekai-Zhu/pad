def solution():
    """Andrew holds a bake sale to fundraise for charity. The bake sale earns a total of $400. Andrew keeps $100 to cover the cost of ingredients. He donates half of the remaining total to the local homeless shelter, and the other half to the local food bank. Andrew also decides to donate $10 from his own piggy bank to the local homeless shelter. How much money in total does Andrew donate to the homeless shelter?"""
    total_earned = 400
    cost_of_ingredients = 100
    remaining_money = total_earned - cost_of_ingredients
    donations = remaining_money / 2 + 10
    result = donations
    return result

print(solution())