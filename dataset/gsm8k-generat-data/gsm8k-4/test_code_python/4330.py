def solution():
    """Simon has 20% more legos than Bruce, who has 20 more than Kent. If Kent has 40 legos, how many does Simon have?"""
    # Define the number of legos Kent has
    kent_legos = 40

    # Calculate the number of legos Bruce has
    bruce_legos = kent_legos + 20

    # Calculate the percentage increase for Simon
    simon_increase = 20 / 100

    # Calculate the number of legos Simon has
    simon_legos = bruce_legos * (1 + simon_increase)

    result = round(simon_legos)
    return result

print(solution())