def solution():
    """Julia bought 3 packs of red balls, 10 packs of yellow balls, and 8 packs of green balls. There were 19 balls in each package. How many balls did Julie buy in all?"""
    # Define the number of packs of each color of balls purchased
    red_packs = 3
    yellow_packs = 10
    green_packs = 8

    # Define the number of balls in each package
    balls_per_package = 19

    # Calculate the total number of balls purchased
    total_balls = (red_packs + yellow_packs + green_packs) * balls_per_package
    
    # Return the result
    result = total_balls
    return result

print(solution())