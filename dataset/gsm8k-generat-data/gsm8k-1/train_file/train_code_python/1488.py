def solution():
    """Seth lost 17.5 pounds. Jerome lost three times that many pounds and Veronica lost 1.5 pounds more than Seth. How many pounds did the 3 people lose in total?"""
    seth_loss = 17.5
    jerome_loss = seth_loss * 3
    veronica_loss = seth_loss + 1.5
    total_loss = seth_loss + jerome_loss + veronica_loss
    result = total_loss
    return result

print(solution())