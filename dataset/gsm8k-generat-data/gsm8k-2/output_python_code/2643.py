def solution():
    """Carl has a goal of selling 96 cupcakes in 2 days. Carl needs to give 24 cupcakes to Bonnie as payment for using her storefront. How many cupcakes must Carl sell per day to reach his goal?"""
    total_cupcakes = 96
    cupcakes_given = 24
    cupcakes_to_sell = total_cupcakes - cupcakes_given
    days_to_sell = 2
    cupcakes_per_day = cupcakes_to_sell / days_to_sell
    result = cupcakes_per_day
    return result

print(solution())