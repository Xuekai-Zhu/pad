def solution():
    """John decides to go back to school to get his PhD. He first takes 1 year of courses to get acclimated back to school life before starting his PhD. After that, he spends 2 years learning the basics of his field. He then starts research, and he spends 75% more time on research than he did learning the basics. He then spends half as long on writing his dissertation as his acclimation period. How long did it take him to do everything?"""
    # Define the time for each step in getting a PhD
    acclimation = 1
    basics = 2
    research = 2.75 * basics
    dissertation = acclimation / 2

    # Add up the time for each step to get the total time required
    total_time = acclimation + basics + research + dissertation

    # Return the result
    result = total_time
    return result

print(solution())