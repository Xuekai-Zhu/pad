def solution():
    """Carla had 400 chickens on her chicken farm. However, 40% of the chicken died due to a certain disease. How many chickens were there if she bought ten times as many chickens as the number that died due to disease?"""
    # Define the initial number of chickens
    initial_chickens = 400

    # Calculate the number of chickens that died
    dead_chickens = initial_chickens * 0.4

    # Calculate the number of chickens that she bought as replacements
    bought_chickens = dead_chickens * 10

    # Calculate the final number of chickens
    final_chickens = initial_chickens - dead_chickens + bought_chickens

    # return the result
    result = final_chickens
    return result

print(solution())