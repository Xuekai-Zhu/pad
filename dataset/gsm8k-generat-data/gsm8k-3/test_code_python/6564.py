def solution():
    """Aimee does a poll around her neighborhood and makes sure to get answers from 50% men and 50% women. She finds that 35% of women are in favor of shortening the school day by 30 minutes. 39 women in her poll opposed this idea. How many people did she poll?"""
    # Define the percentage of women in the poll
    PERCENT_WOMEN = 50

    # Define the percentage of women in favor of shortening the school day
    PERCENT_WOMEN_IN_FAVOR = 35

    # Define the number of women who opposed the idea
    WOMEN_OPPOSED = 39

    # Calculate the total number of women in the poll
    total_women = WOMEN_OPPOSED / (1 - PERCENT_WOMEN_IN_FAVOR/100)

    # Calculate the total number of people in the poll
    total_people = total_women / (PERCENT_WOMEN/100)

    # Display the total number of people in the poll
    result = total_people
    return result

print(solution())