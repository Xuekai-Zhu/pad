def solution():
    """Megan is an actress. She was the lead actress in 80% of her work. In total, Megan participated in 100 plays. How many times Megan was not the lead actress?"""
    total_plays = 100
    lead_actress_percentage = 80
    lead_actress_plays = total_plays * (lead_actress_percentage/100)
    not_lead_actress_plays = total_plays - lead_actress_plays
    result = not_lead_actress_plays
    return result

print(solution())