def solution():
    
    # Define the prices of almonds and walnuts
    almonds_price = 10
    walnuts_price = 15

    # Calculate the cost of a mixture of 1/2 pound almonds and 1/3 pound walnuts
    mixture_cost_1_5 = almonds_price * (1/5)
    mixture_cost_1_3 = walnuts_price * (1/3)

    # Calculate the difference in cost between the mixture of 1/2 pound almonds and 1/3 pound walnuts and the mixture
    cost_difference = mixture_cost_1_5 - mixture_cost_1_3

    # return the result
    result = cost_difference
    return result

print(solution())