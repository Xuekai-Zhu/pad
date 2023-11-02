def solution():
    """Seth lost 17.5 pounds. Jerome lost three times that many pounds and Veronica lost 1.5 pounds more than Seth. How many pounds did the 3 people lose in total?"""

    # Define the weight lost by Seth
    seth_weight_lost = 17.5

    # Calculate the weight lost by Jerome
    jerome_weight_lost = seth_weight_lost * 3

    # Calculate the weight lost by Veronica
    veronica_weight_lost = seth_weight_lost + 1.5

    # Calculate the total weight lost by the three people
    total_weight_lost = seth_weight_lost + jerome_weight_lost + veronica_weight_lost

    result = total_weight_lost
    return result

print(solution())