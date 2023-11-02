def solution():
    """John had $200. He gave 3/8 of his money to his mother and 3/10 to his father. How much money did John have left?"""
    # Define John's initial amount of money
    john_money = 200

    # Calculate the amount of money given to John's mother
    mother_money = john_money * 3/8

    # Calculate the amount of money given to John's father
    father_money = john_money * 3/10

    # Calculate the total amount of money John gave away
    total_given = mother_money + father_money

    # Calculate the amount of money John has left
    john_money_left = john_money - total_given

    # Return the result
    result = john_money_left
    return result

print(solution())