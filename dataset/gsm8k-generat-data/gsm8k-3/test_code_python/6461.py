def solution():
    """John had $200. He gave 3/8 of his money to his mother and 3/10 to his father. How much money did John have left?"""
    # Define John's starting amount of money
    john_money = 200

    # Calculate how much John gave to his mother
    mother_money = john_money * (3/8)

    # Calculate how much John gave to his father
    father_money = john_money * (3/10)

    # Calculate how much money John has left
    remaining_money = john_money - mother_money - father_money

    # Display how much money John has left
    result = remaining_money
    return result

print(solution())