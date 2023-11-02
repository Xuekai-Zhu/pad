def solution():
    """Milo's parents tell him that he can win cash rewards for good grades. He will get $5 times the average grade he gets. He gets three 2s, four 3s, a 4, and a 5. How much cash does he get?"""
    # Define the grades and their weights
    grades = [2, 2, 2, 3, 3, 3, 3, 4, 5]
    weights = [2, 2, 2, 3, 3, 3, 3, 4, 5]

    # Calculate the weighted average
    weighted_sum = sum([grades[i]*weights[i] for i in range(len(grades))])
    weight_sum = sum(weights)
    average = weighted_sum / weight_sum

    # Calculate the cash reward
    cash_reward = average * 5

    # Return the cash reward
    result = cash_reward
    return result

print(solution())