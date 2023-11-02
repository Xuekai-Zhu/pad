def solution():
    """Aimee does a poll around her neighborhood and makes sure to get answers from 50% men and 50% women. She finds that 35% of women are in favor of shortening the school day by 30 minutes. 39 women in her poll opposed this idea. How many people did she poll?"""
    women_in_favor = 0.35
    women_opposed = 39
    total_women = women_opposed / (1 - women_in_favor)
    total_people = 2 * total_women
    result = total_people
    return result

print(solution())