def solution():
    dots_per_blouse = 20  # Each blouse gets 20 dots
    ml_per_dot = 10  # Each dot takes 10 ml of dye
    ml_per_bottle = 400  # Each bottle contains 400 ml of dye
    blouses_to_dye = 100  # Jenna needs to dye 100 blouses

    # Calculate the total ml of dye Jenna needs to buy
    total_ml_of_dye = dots_per_blouse * ml_per_dot * blouses_to_dye

    # Calculate the number of bottles of dye Jenna needs to buy
    bottles_of_dye = total_ml_of_dye / ml_per_bottle
    result = bottles_of_dye
    return result

print(solution())