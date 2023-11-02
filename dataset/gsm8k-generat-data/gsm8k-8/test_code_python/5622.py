def solution():
    # Define the weight lost in March and April
    march_loss = 3
    april_loss = 4

    # Calculate the total weight lost so far
    total_loss = march_loss + april_loss

    # Calculate the weight Michael needs to lose in May to meet his goal
    remaining_loss = 10 - total_loss

    result = remaining_loss
    return result

print(solution())