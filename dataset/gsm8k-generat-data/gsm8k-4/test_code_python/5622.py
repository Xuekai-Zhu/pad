def solution():
    """Michael wants to lose 10 pounds by June. He lost 3 pounds in March and 4 pounds in April. How much weight does he have to lose in May to meet his goal?"""
    # Define the target weight loss and the weight lost in March and April
    target_loss = 10
    march_loss = 3
    april_loss = 4

    # Calculate the total weight lost so far
    total_loss = march_loss + april_loss

    # Calculate the weight loss needed in May to meet the target
    may_loss = target_loss - total_loss

    # Return the result
    result = may_loss
    return result

print(solution())