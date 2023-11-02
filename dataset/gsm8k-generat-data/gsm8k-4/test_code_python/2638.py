def solution():
    """Bridge and Sarah have $3 between them. If Bridget has 50 cents more than Sarah, how many cents does Sarah have?"""
    # Define the total amount of money they have in cents
    total_money = 300

    # Calculate the amount of money Bridget has in cents
    bridgit_money = (total_money + 50) / 2

    # Calculate the amount of money Sarah has in cents
    sarah_money = total_money - bridgit_money

    result = sarah_money
    return result

print(solution())