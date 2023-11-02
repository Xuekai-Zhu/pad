def solution():
    # Initial number of phones
    initial_phones = 20

    # Number of defective phones
    defective_phones = 5

    # Number of non-defective phones
    non_defective_phones = initial_phones - defective_phones

    # Number of phones sold to customer A
    phones_sold_to_a = 3

    # Number of phones sold to customer C
    phones_sold_to_c = 7

    # Total number of phones sold to customers A and C
    total_sold = phones_sold_to_a + phones_sold_to_c

    # Number of phones sold to customer B
    phones_sold_to_b = non_defective_phones - total_sold

    result = phones_sold_to_b
    return result

print(solution())