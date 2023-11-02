def solution():
    # Calculate the amount of money Susan has left after shopping
    left_after_clothes = 600 / 2  # Susan spent half of her money on clothes
    left_after_books = left_after_clothes / 2  # Susan spent half of what was left after buying clothes on books
    result = left_after_books
    return result

print(solution())