def solution():
    """A lorry is 500 pounds when empty. What will its weight be if it's loaded with 20 bags of apples, each weighing 60 pounds?"""
    empty_weight = 500
    bags_of_apples = 20
    weight_per_bag = 60
    total_weight = empty_weight + (bags_of_apples * weight_per_bag)
    result = total_weight
    return result

print(solution())