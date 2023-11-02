def solution():
    """Mr Cruz went to his doctor to seek advice on the best way to gain weight. His doctor told him to include more proteins in his meals and live a generally healthy lifestyle. After a month of following his doctor's advice, Mr Cruz had a weight gain of 20 pounds. He gained 30 more pounds in the second month after more healthy eating habits. If he originally weighed 70 pounds, what's his weight after the two months?"""
    # Define Mr Cruz's initial weight
    initial_weight = 70

    # Define the weight gains in the first and second months
    weight_gain_1 = 20
    weight_gain_2 = 30

    # Calculate Mr Cruz's weight after the two months
    total_weight_gain = weight_gain_1 + weight_gain_2
    final_weight = initial_weight + total_weight_gain

    # Display Mr Cruz's weight after the two months
    result = final_weight
    return result

print(solution())