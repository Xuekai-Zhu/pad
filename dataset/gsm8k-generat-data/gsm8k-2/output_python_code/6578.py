def solution():
    """Megan is an actress. She was the lead actress in 80% of her work. In total, Megan participated in 100 plays. How many times Megan was not the lead actress?"""
    total_plays = 100
    lead_plays = total_plays * 0.8
    non_lead_plays = total_plays - lead_plays
    result = non_lead_plays
    return result

print(solution())