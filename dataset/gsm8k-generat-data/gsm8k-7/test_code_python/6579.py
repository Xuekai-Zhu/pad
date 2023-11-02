def solution():
    total_plays = 100
    lead_percentage = 0.8

    # Calculate the number of plays where Megan was the lead actress
    lead_plays = total_plays * lead_percentage

    # Calculate the number of plays where Megan was not the lead actress
    non_lead_plays = total_plays - lead_plays
    result = non_lead_plays
    return result

print(solution())