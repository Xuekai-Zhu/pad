def solution():
    num_phones = 3  # John and his 2 kids
    phone_price = 600  # The phone price is $600

    # Calculate the total cost of the phones before the first 2
    total_cost_before_2_phones = num_phones * phone_price

    # Calculate the total cost of the phones after the first 2
    total_cost_after_2_phones = total_cost_before_2_phones * 2

    # Calculate the total cost of all phones
    total_cost = total_cost_after_2_phones + total_cost_after_2_phones
    result = total_cost
    return result

print(solution())