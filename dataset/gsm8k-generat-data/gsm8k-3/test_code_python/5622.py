def solution():
    """Michael wants to lose 10 pounds by June. He lost 3 pounds in March and 4 pounds in April. How much weight does he have to lose in May to meet his goal?"""
    # Define the total weight Michael wants to lose and the weight he has already lost
    TOTAL_LOSS = 10
    LOST_SO_FAR = 3 + 4

    # Calculate the weight Michael needs to lose in May to meet his goal
    weight_to_lose = TOTAL_LOSS - LOST_SO_FAR

    # Display the weight Michael needs to lose in May
    result = weight_to_lose
    return result

print(solution())