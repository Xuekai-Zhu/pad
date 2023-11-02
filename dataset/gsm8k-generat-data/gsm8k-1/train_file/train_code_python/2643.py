def solution():
    """Carl has a goal of selling 96 cupcakes in 2 days. Carl needs to give 24 cupcakes to Bonnie as payment for using her storefront. How many cupcakes must Carl sell per day to reach his goal?"""
    total_cupcakes = 96
    cupcakes_given = 24
    days = 2
    cupcakes_goal = (total_cupcakes - cupcakes_given) / days
    result = cupcakes_goal
    return result

print(solution())