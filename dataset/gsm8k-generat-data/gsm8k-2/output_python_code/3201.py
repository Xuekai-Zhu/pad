def solution():
    """Milly's babysitter charges $16/hour. Milly is considering switching to a new babysitter who charges $12/hour, but also charges an extra $3 for each time the kids scream at her. If Milly usually hires the babysitter for 6 hours, and her kids usually scream twice per babysitting gig, how much less will the new babysitter cost?"""
    current_babysitter_cost = 16 * 6
    new_babysitter_cost = 12 * 6 + 3 * 2
    amount_saved = current_babysitter_cost - new_babysitter_cost
    result = amount_saved
    return result

print(solution())