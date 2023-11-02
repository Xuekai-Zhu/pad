def solution():
    # Define variables
    wanda_bread = 90
    wanda_treats = 0.5 * (wanda_bread / 3)
    jane_treats = wanda_treats * (1 / 0.75)
    jane_bread = 0.75 * jane_treats

    # Calculate total number of bread and treats
    total_bread = wanda_bread + jane_bread
    total_treats = wanda_treats + jane_treats
    total_food = total_bread + total_treats
    result = total_food
    return result

print(solution())