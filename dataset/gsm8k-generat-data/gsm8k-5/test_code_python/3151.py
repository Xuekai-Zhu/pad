def solution():
    money_left = 130  # Jason was left with $130 at the end
    amount_spent_on_dvds = 8  # Jason spent an additional $8 on some DVDs
    fraction_left_after_books = 3/4  # Jason spent 1/4 of his money on books, so he has 3/4 left

    # Calculate the total amount spent on books and the initial amount of money
    amount_spent_on_books = (1/4) * (1/fraction_left_after_books) * money_left - 10
    initial_money = money_left + amount_spent_on_dvds + amount_spent_on_books

    # Calculate the amount of money left after spending 2/5 of the remaining money
    money_left_after_dvds = (3/5) * (1/fraction_left_after_books) * initial_money - 8

    # Check if the final amount of money left matches the given value
    if money_left_after_dvds == money_left:
        result = initial_money
    else:
        result = "Unable to calculate the initial amount of money"

    return result

print(solution())