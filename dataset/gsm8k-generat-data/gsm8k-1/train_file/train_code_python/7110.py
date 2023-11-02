def solution():
    """Jerry finds six hawk feathers and 17 times as many eagle feathers as hawk feathers. If he gives 10 feathers to his sister and sells half the remaining feathers, how many does he have left?"""
    hawk_feathers = 6
    eagle_feathers = hawk_feathers * 17
    total_feathers = hawk_feathers + eagle_feathers
    feathers_given_away = 10
    remaining_feathers = total_feathers - feathers_given_away
    feathers_sold = remaining_feathers / 2
    feathers_left = remaining_feathers - feathers_sold
    result = feathers_left
    return result

print(solution())