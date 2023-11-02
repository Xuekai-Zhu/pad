def solution():
    """It takes 50 minutes to cut a woman's hair, 15 minutes to cut a man's hair, and 25 minutes to cut a kid's hair.  If Joe cut 3 women's, 2 men's, and 3 children's hair, how much time did he spend cutting hair?"""
    # Define the time it takes to cut each type of hair
    WOMAN_TIME = 50
    MAN_TIME = 15
    KID_TIME = 25

    # Define the number of each type of hair Joe cut
    women_hair = 3
    men_hair = 2
    kids_hair = 3

    # Calculate the total time spent cutting hair
    total_time = (women_hair * WOMAN_TIME) + (men_hair * MAN_TIME) + (kids_hair * KID_TIME)

    # Display the total time spent cutting hair
    result = total_time
    return result

print(solution())