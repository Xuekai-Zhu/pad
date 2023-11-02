def solution():
    """Carla had 400 chickens on her chicken farm. However, 40% of the chicken died due to a certain disease. How many chickens were there if she bought ten times as many chickens as the number that died due to disease?"""
    # Calculate the number of chickens that died due to disease
    chicken_deaths = 0.4 * 400

    # Calculate the number of chickens Carla bought to replace the ones that died
    new_chickens = 10 * chicken_deaths

    # Calculate the total number of chickens on the farm now
    total_chickens = 400 - chicken_deaths + new_chickens

    # Display the total number of chickens
    result = total_chickens
    return result

print(solution())