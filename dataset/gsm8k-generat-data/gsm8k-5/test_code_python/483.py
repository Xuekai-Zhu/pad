def solution():
    initial_weight = 156  # Andy's weight at the beginning of the year
    growth_inches = 3  # Andy grew by 3 inches
    growth_weight = 36  # Andy gained 36 pounds

    # Calculate Andy's new weight after growth
    height_in_inches = 68 + growth_inches  # Andy's height in inches after growth
    weight_after_growth = 110 + (height_in_inches - 60) * 2.3  # Andy's weight after growth

    # Calculate Andy's weight after exercise
    monthly_loss = growth_weight / 8  # Andy lost an eighth of his weight each month
    weight_after_exercise = weight_after_growth - 3 * monthly_loss  # Andy exercised for 3 months

    # Calculate how much less Andy weighs now than at the beginning of the year
    weight_loss = initial_weight - weight_after_exercise
    result = weight_loss
    return result

print(solution())