def solution():
    total_plays = 100  # Megan participated in 100 plays
    lead_actress_plays = total_plays * 0.8  # Megan was the lead actress in 80% of her work
    not_lead_actress_plays = total_plays - lead_actress_plays  # Calculate the number of times Megan was not the lead actress
    result = not_lead_actress_plays
    return result

print(solution())