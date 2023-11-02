def solution():
    # Define the total amount owned
    total_amount = 250

    # Calculate the amount owned by Ali
    ali_amount = (total_amount - 40) / 2

    # Calculate the amount owned by James
    james_amount = ali_amount + 40
    result = james_amount
    return result

print(solution())