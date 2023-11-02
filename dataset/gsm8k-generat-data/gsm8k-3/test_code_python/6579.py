def solution():
    """Megan is an actress. She was the lead actress in 80% of her work. In total, Megan participated in 100 plays. How many times Megan was not the lead actress?"""
    # Define the percentage of plays Megan was the lead actress in
    lead_percentage = 0.8

    # Define the total number of plays Megan participated in
    total_plays = 100

    # Calculate the number of times Megan was the lead actress
    lead_plays = int(total_plays * lead_percentage)

    # Calculate the number of times Megan was not the lead actress
    not_lead_plays = total_plays - lead_plays

    # Display the number of times Megan was not the lead actress
    result = not_lead_plays
    return result

print(solution())