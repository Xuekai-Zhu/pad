def solution():
    """Jenna is adding black dots to a bunch of white blouses. Each blouse gets 20 dots, and each dot takes 10 ml of black dye. How many 400-ml bottles of dye does Jenna need to buy to dye 100 blouses?"""
    dots_per_blouse = 20
    ml_per_dot = 10
    total_ml = dots_per_blouse * ml_per_dot * 100
    bottles_needed = total_ml / 400
    result = bottles_needed
    return result

print(solution())