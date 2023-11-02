def solution():
    """Brian can only hold his breath underwater for 10 seconds.  He wants to get better, so he starts practicing.  After a week, he's doubled the amount of time he can do it.  After another week, he's doubled it again from the previous week.  The final week, he's increased it by 50% from the previous week.  How long can Brian hold his breath for now?"""
    # Define Brian's starting time and calculate his progress after each week of practice
    time = 10
    time *= 2  # After week 1
    time *= 2  # After week 2
    time *= 1.5  # After week 3

    # Display Brian's current breath-holding time
    result = time
    return result

print(solution())