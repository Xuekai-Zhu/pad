def solution():
    # Calculate the total amount Alexis spent
    total_spent = 30 + 46 + 38 + 11 + 18 + 16  # including the $16 left from her budget
    # Calculate the amount Alexis paid for the shoes
    shoes_cost = 200 - total_spent  # the difference between her budget and the total amount spent
    result = shoes_cost
    return result

print(solution())