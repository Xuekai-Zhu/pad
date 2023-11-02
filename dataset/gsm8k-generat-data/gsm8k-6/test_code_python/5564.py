def solution():
    # Calculate the amount of money raised by Miss Rollin's class
    total_amount = 2300 / (2/1) * 8 * 3  # Mrs. Johnson's class raised twice as much as Mrs. Sutton's class, Mrs. Sutton's class raised 8 times less than Miss Rollin's class, and Miss Rollin's class raised a third of the total amount raised
    # Calculate the amount of money after deducting administration fees
    final_amount = total_amount * (1 - 0.02)  # 2% will be deducted for administration fees
    result = final_amount
    return result

print(solution())