def solution():
    """Jenna is adding black dots to a bunch of white blouses. Each blouse gets 20 dots, and each dot takes 10 ml of black dye. How many 400-ml bottles of dye does Jenna need to buy to dye 100 blouses?"""
    dots_per_blouse = 20
    ml_per_dot = 10
    blouses = 100
    total_dots = dots_per_blouse * blouses
    total_ml = total_dots * ml_per_dot
    bottles = total_ml // 400 + 1  # add one bottle to cover any remaining ml
    result = bottles
    return result

print(solution())