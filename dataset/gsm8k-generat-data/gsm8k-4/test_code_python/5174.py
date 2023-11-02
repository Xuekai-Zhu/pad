def solution():
    """Alex needs to be 54 inches tall to ride the newest roller coaster at the theme park. He is 48 inches tall this year. 
    He hears a rumor that for every hour he hangs upside down, he can grow 1/12 of an inch. Normally he grows 1/3 of an inch per month. 
    On average, how many hours does he need to hang upside down each month to be tall enough next year to ride the rollercoaster?"""
    # Define Alex's starting height, the required height to ride the roller coaster, and the normal monthly growth rate
    starting_height = 48
    required_height = 54
    normal_growth_rate = 1/3

    # Define the growth rate per hour of hanging upside down
    upside_down_growth_rate = 1/12

    # Calculate the total growth required by Alex to reach the required height
    total_growth_required = required_height - starting_height

    # Calculate the total growth achieved by Alex per month including hanging upside down and normal growth
    total_growth_per_month = normal_growth_rate + (upside_down_growth_rate * x)

    # Calculate the number of hours Alex needs to hang upside down each month to achieve the required growth rate
    x = total_growth_required / upside_down_growth_rate / 12 - normal_growth_rate

    result = round(x)
    return result

print(solution())