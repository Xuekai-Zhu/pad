def solution():
    """Ryan is looking for people to crowdfund his new business idea. If the average person funds $10 to a project they're interested in, how many people will Ryan have to recruit to fund a $1,000 business if he has $200 already?"""
    # Define the amount of money Ryan needs to raise and the amount he already has
    target_amount = 1000
    current_amount = 200

    # Calculate the amount of money Ryan still needs to raise
    remaining_amount = target_amount - current_amount

    # Calculate the number of people Ryan needs to recruit
    num_people = remaining_amount / 10

    # Round up to the nearest integer
    num_people = int(num_people + 0.5)

    # Return the result
    result = num_people
    return result

print(solution())