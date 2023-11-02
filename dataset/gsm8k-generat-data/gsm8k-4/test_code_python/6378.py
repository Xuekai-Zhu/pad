def solution():
    """All 20 of Grant’s baby teeth have fallen out and he has a total of $54 from the tooth fairy. Every time he lost a tooth, he put it under his pillow for the tooth fairy, except for one that he dropped on the way home from school and another he swallowed accidentally. The tooth fairy left Grant $20 when he lost his first tooth. How much did the tooth fairy leave him per tooth after his first tooth, assuming equal money exchanged for each tooth thereafter?"""
    # Define the initial amount and number of teeth lost
    initial_amt = 20
    initial_lost = 1

    # Subtract the amount of money left for the first tooth
    total_amt = 54 - 20

    # Subtract the number of teeth that weren't put under his pillow
    total_lost = 20 - 2

    # Calculate the amount left for each tooth after the first one
    amount_per_tooth = total_amt / total_lost

    # Display the result
    result = amount_per_tooth
    return result

print(solution())