def solution():
    """Seth lost 17.5 pounds. Jerome lost three times that many pounds and Veronica lost 1.5 pounds more than Seth. How many pounds did the 3 people lose in total?"""
    seth_weight = 17.5
    jerome_weight = 3 * seth_weight
    veronica_weight = seth_weight + 1.5
    total_weight_loss = seth_weight + jerome_weight + veronica_weight
    result = total_weight_loss
    return result

print(solution())