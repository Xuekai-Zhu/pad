def solution():
    """Megan is an actress. She was the lead actress in 80% of her work. In total, Megan participated in 100 plays. How many times Megan was not the lead actress?"""
    # Define the total number of plays and the percentage of plays Megan was the lead actress in
    total_plays = 100
    lead_percentage = 0.8

    # Calculate the number of plays Megan was the lead actress in
    lead_plays = total_plays * lead_percentage

    # Calculate the number of plays Megan was not the lead actress in
    not_lead_plays = total_plays - lead_plays

    # return the result
    result = not_lead_plays
    return result

print(solution())