def solution():
    """Aimee does a poll around her neighborhood and makes sure to get answers from 50% men and 50% women. She finds that 35% of women are in favor of shortening the school day by 30 minutes. 39 women in her poll opposed this idea. How many people did she poll?"""
    percent_women = 50
    percent_men = 50
    women_in_favor = 35
    women_opposed = 39
    total_women = 100
    total_people = (total_women / percent_women) * 100
    women_in_poll = total_people * (percent_women / 100)
    women_in_favor_poll = women_in_poll * (women_in_favor / 100)
    total_opposed = women_opposed
    total_in_favor = women_in_favor_poll
    total_unsure = women_in_poll - women_in_favor_poll - women_opposed
    result = total_people
    return result

print(solution())