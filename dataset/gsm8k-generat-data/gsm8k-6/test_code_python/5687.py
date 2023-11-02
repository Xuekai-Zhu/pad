def solution():
    # Calculate the total cost of white T-shirts
    white_T_shirts_price = 3 * 5  # Each pack of white T-shirts costs $3 and contains 5 T-shirts
    total_white_T_shirts_price = white_T_shirts_price * 2  # Maddie bought 2 packs of white T-shirts

    # Calculate the total cost of blue T-shirts
    blue_T_shirts_price = 3 * 3  # Each pack of blue T-shirts costs $3 and contains 3 T-shirts
    total_blue_T_shirts_price = blue_T_shirts_price * 4  # Maddie bought 4 packs of blue T-shirts

    # Calculate the total amount Maddie spent
    total_spent = total_white_T_shirts_price + total_blue_T_shirts_price
    result = total_spent
    return result

print(solution())