def solution():
    """Jerry finds six hawk feathers and 17 times as many eagle feathers as hawk feathers. If he gives 10 feathers to his sister and sells half the remaining feathers, how many does he have left?"""
    hawk_feathers = 6
    eagle_feathers = 17 * hawk_feathers
    total_feathers = hawk_feathers + eagle_feathers
    total_feathers -= 10
    remaining_feathers = total_feathers // 2
    result = remaining_feathers
    return result

print(solution())