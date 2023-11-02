def solution():
    """Ryan is looking for people to crowdfund his new business idea.  If the average person funds $10 to a project they're interested in, how many people will Ryan have to recruit to fund a $1,000 business if he has $200 already?"""
    # Define the total amount of money needed
    total_money_needed = 1000

    # Define the amount of money Ryan already has
    money_already_have = 200

    # Calculate the remaining amount of money needed
    remaining_money_needed = total_money_needed - money_already_have

    # Calculate the number of people needed to fund the remaining amount of money
    number_of_people_needed = remaining_money_needed / 10

    # Round up the number of people needed to get a whole number
    number_of_people_needed = math.ceil(number_of_people_needed)

    # Display the number of people needed
    result = number_of_people_needed
    return result

print(solution())