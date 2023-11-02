def solution():
    """Mary tried to improve her health by changing her diet, but her weight bounced like a yo-yo.  At first, she dropped a dozen pounds. Then, she added back twice the weight that she initially lost.  Then, she dropped three times more weight than she initially had lost.  But finally, she gained back half of a dozen pounds.  If she weighed 99 pounds at the start of her change in diet, what was her final weight, in pounds?"""
    # Define the initial weight of Mary
    initial_weight = 99

    # Calculate the weight after losing a dozen pounds
    weight_after_losing_dozen = initial_weight - 12

    # Calculate the weight after adding back twice the weight that was initially lost
    weight_after_adding_twice = weight_after_losing_dozen + (2 * 12)

    # Calculate the weight after dropping three times more weight than initially lost
    weight_after_dropping_three_times_more = weight_after_adding_twice - (3 * 12)

    # Calculate the weight after gaining back half a dozen pounds
    weight_after_gaining_half_dozen = weight_after_dropping_three_times_more + (0.5 * 12)

    # Display the final weight of Mary
    result = weight_after_gaining_half_dozen
    return result

print(solution())