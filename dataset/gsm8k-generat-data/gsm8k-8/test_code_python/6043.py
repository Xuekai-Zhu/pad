def solution():
    # Define the weight and value of one gold quarter
    weight_per_quarter = 1/5
    value_per_quarter = 100 * weight_per_quarter

    # Calculate the total value of Carlos' gold quarters if he spends them
    total_value_if_spent = value_per_quarter * number_of_quarters

    # Calculate the total value of Carlos' gold quarters if he melts them down
    total_weight = weight_per_quarter * number_of_quarters
    total_value_if_melted = total_weight * 100

    # Calculate how many times more money Carlos would get from melting down the gold quarters
    times_more_money = total_value_if_melted / total_value_if_spent
    result = times_more_money
    return result

print(solution())