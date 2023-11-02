def solution():
    # Define the initial amount of money Susan earned
    initial_amount = 600

    # Calculate the amount spent on clothes
    clothes_spending = initial_amount / 2

    # Calculate the amount left after clothes shopping
    left_after_clothes = initial_amount - clothes_spending

    # Calculate the amount spent on books
    books_spending = left_after_clothes / 2

    # Calculate the final amount Susan has left
    final_amount_left = left_after_clothes - books_spending
    result = final_amount_left
    return result

print(solution())