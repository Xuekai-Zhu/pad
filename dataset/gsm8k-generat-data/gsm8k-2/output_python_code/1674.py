def solution():
    """A lorry is 500 pounds when empty. What will its weight be if it's loaded with 20 bags of apples, each weighing 60 pounds?"""
    empty_weight = 500
    bags_weight = 20 * 60
    total_weight = empty_weight + bags_weight
    result = total_weight
    return result

print(solution())