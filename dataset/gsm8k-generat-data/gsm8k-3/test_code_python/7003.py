def solution():
    """Julia bought 3 packs of red balls, 10 packs of yellow balls, and 8 packs of green balls. There were 19 balls in each package. How many balls did Julie buy in all?"""
    # Define the number of packs purchased and the number of balls per pack
    red_packs = 3
    yellow_packs = 10
    green_packs = 8
    balls_per_pack = 19

    # Calculate the total number of balls purchased
    total_balls = (red_packs + yellow_packs + green_packs) * balls_per_pack

    # Display the total number of balls purchased
    result = total_balls
    return result

print(solution())