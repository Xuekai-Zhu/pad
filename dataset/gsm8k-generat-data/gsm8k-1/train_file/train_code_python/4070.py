def solution():
    """Mr Cruz went to his doctor to seek advice on the best way to gain weight. His doctor told him to include more proteins in his meals and live a generally healthy lifestyle. After a month of following his doctor's advice, Mr Cruz had a weight gain of 20 pounds. He gained 30 more pounds in the second month after more healthy eating habits. If he originally weighed 70 pounds, what's his weight after the two months?"""
    initial_weight = 70
    first_month_gain = 20
    second_month_gain = 30
    new_weight = initial_weight + first_month_gain + second_month_gain
    result = new_weight
    return result

print(solution())