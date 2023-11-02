def solution():
    """Mr Cruz went to his doctor to seek advice on the best way to gain weight. His doctor told him to include more proteins in his meals and live a generally healthy lifestyle. After a month of following his doctor's advice, Mr Cruz had a weight gain of 20 pounds. He gained 30 more pounds in the second month after more healthy eating habits. If he originally weighed 70 pounds, what's his weight after the two months?"""
    # Define the initial weight and the amount gained in the first month
    initial_weight = 70
    first_month_gain = 20

    # Calculate the weight after the first month
    weight_after_first_month = initial_weight + first_month_gain

    # Calculate the total amount gained in the two months
    total_gain = first_month_gain + 30

    # Calculate the final weight after the two months
    final_weight = initial_weight + total_gain

    # return the result
    result = final_weight
    return result

print(solution())