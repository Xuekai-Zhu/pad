def solution():
    bowl_capacity = 16
    initial_amount = bowl_capacity / 2
    amount_added = 4
    amount_removed = 2
    final_amount = bowl_capacity

    # Calculate the total amount of punch that Mark added initially
    total_added = initial_amount + amount_added - amount_removed + final_amount

    result = total_added
    return result

print(solution())