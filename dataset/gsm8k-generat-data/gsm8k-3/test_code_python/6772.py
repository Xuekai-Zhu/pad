def solution():
    """A group of friends walked into Juju’s Juice Bar ordered a glass of fruit juice each. They spent a total of $94. Some of them ordered mango juice, which sells for $5 a glass, while others asked for pineapple juice, at $6 a glass. If $54 was spent on pineapple juice, how many people were in the group?"""
    # Define the cost of each type of juice
    MANGO_PRICE = 5
    PINEAPPLE_PRICE = 6

    # Define the total amount spent and the amount spent on pineapple juice
    total_spent = 94
    pineapple_spent = 54

    # Calculate the total number of glasses of juice purchased
    total_glasses = (total_spent - pineapple_spent) / MANGO_PRICE + pineapple_spent / PINEAPPLE_PRICE

    # Calculate the number of people in the group
    num_people = total_glasses

    # Display the number of people in the group
    result = num_people
    return result

print(solution())