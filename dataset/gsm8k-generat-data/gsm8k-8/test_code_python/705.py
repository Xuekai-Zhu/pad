def solution():
    # Define the final amount of money
    final_amount = 51

    # Calculate the amount of money Isabel had before buying the book
    remaining_money = final_amount * 2
    total_money_before_book = remaining_money

    # Calculate the amount of money Isabel had before buying the toy
    remaining_money *= 2
    total_money_before_toy = remaining_money

    # Calculate the initial amount of money Isabel had
    initial_money = total_money_before_toy * 2
    result = initial_money
    return result

print(solution())