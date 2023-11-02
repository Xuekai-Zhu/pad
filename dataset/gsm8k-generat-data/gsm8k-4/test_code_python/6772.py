def solution():
    """A group of friends walked into Juju’s Juice Bar ordered a glass of fruit juice each.
    They spent a total of $94. Some of them ordered mango juice, which sells for $5 a glass,
    while others asked for pineapple juice, at $6 a glass.
    If $54 was spent on pineapple juice, how many people were in the group?"""
    
    # Define the price of mango and pineapple juice and the total amount spent
    mango_price = 5
    pineapple_price = 6
    total_spent = 94

    # Calculate the number of glasses of pineapple juice ordered
    pineapple_glasses = 54 // pineapple_price

    # Calculate the number of glasses of mango juice ordered
    mango_glasses = (total_spent - (pineapple_glasses * pineapple_price)) // mango_price

    # Calculate the total number of glasses ordered
    total_glasses = pineapple_glasses + mango_glasses

    # Calculate the number of people in the group
    num_people = total_glasses

    result = num_people
    return result

print(solution())