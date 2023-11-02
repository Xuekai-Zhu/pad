def solution():
    """All 20 of Grant’s baby teeth have fallen out and he has a total of $54 from the tooth fairy. Every time he lost a tooth, he put it under his pillow for the tooth fairy, except for one that he dropped on the way home from school and another he swallowed accidentally. The tooth fairy left Grant $20 when he lost his first tooth. How much did the tooth fairy leave him per tooth after his first tooth, assuming equal money exchanged for each tooth thereafter?"""
    # Define the total amount of money left by the tooth fairy
    total_money = 54

    # Define the number of teeth that Grant lost
    num_teeth = 20 - 2  # Subtract the 2 missing teeth

    # Calculate the amount of money left per tooth after the first tooth
    money_per_tooth = (total_money - 20) / num_teeth

    # Display the amount of money left per tooth after the first tooth
    result = money_per_tooth
    return result

print(solution())