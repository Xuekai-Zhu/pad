def solution():
    num_phones = 5
    phone_price = 700
    total_paid = 4000

    # Calculate the total cost of all phones
    total_phones_cost = num_phones * phone_price

    # Calculate the amount of change the seller will receive
    change = total_paid - total_phones_cost
    result = change
    return result

print(solution())