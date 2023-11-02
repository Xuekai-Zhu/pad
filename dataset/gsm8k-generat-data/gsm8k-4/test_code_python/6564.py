def solution():
    """Aimee does a poll around her neighborhood and makes sure to get answers from 50% men and 50% women. She finds that 35% of women are in favor of shortening the school day by 30 minutes. 39 women in her poll opposed this idea. How many people did she poll?"""
    # Define the percentage of women who are in favor of shortening the school day
    women_in_favor_percentage = 0.35

    # Define the number of women who opposed the idea
    women_opposed = 39

    # Calculate the number of women who are in favor of shortening the school day
    women_in_favor = (1 - women_opposed / 0.5) * 0.5 * women_in_favor_percentage

    # Calculate the total number of people polled
    total_poll = 2 * women_in_favor / women_in_favor_percentage

    # return the result
    result = int(total_poll)
    return result

print(solution())