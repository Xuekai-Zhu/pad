def solution():
    
    # Define the initial weight loss and the weight gain for each breakfast
    initial_loss = 1.25
    initial_gain = 1.75

    # Calculate the weight loss and the weight gain for each breakfast
    weight_loss = initial_loss * 7 * 5
    weight_gain = initial_gain * 7 * 5

    # Calculate the difference in weight loss and weight gain
    weight_difference = weight_loss - weight_gain

    # return the result
    result = weight_difference
    return result

print(solution())