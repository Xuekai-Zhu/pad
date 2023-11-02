def solution():
    """Carl has a goal of selling 96 cupcakes in 2 days. Carl needs to give 24 cupcakes to Bonnie as payment for using her storefront. How many cupcakes must Carl sell per day to reach his goal?"""
    # Define the total number of cupcakes Carl needs to sell and the number he needs to give to Bonnie
    total_cupcakes = 96
    cupcakes_to_bonnie = 24

    # Calculate the number of cupcakes Carl needs to sell each day to reach his goal
    cupcakes_per_day = (total_cupcakes - cupcakes_to_bonnie) / 2

    result = cupcakes_per_day
    return result

print(solution())