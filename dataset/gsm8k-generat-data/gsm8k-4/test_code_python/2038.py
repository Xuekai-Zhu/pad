def solution():
    """It takes 50 minutes to cut a woman's hair, 15 minutes to cut a man's hair, and 25 minutes to cut a kid's hair.  If Joe cut 3 women's, 2 men's, and 3 children's hair, how much time did he spend cutting hair?"""
    # Define the time to cut each type of hair
    women_time = 50
    men_time = 15
    kids_time = 25

    # Define the number of each type of haircuts
    women_cuts = 3
    men_cuts = 2
    kids_cuts = 3

    # Calculate the total time spent cutting hair
    total_time = women_time * women_cuts + men_time * men_cuts + kids_time * kids_cuts

    # Format the time in hours and minutes
    hours = total_time // 60
    minutes = total_time % 60

    # Return the result
    result = f"{hours} hours {minutes} minutes"
    return result

print(solution())