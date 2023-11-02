def solution():
    """A store is selling mobile phones. This store contains 20 units of phones but the owner found out that there were 5 defective units. After he got rid of the defective units, he started to sell the rest of his units to customer A who bought 3 units, customer B who bought a certain amount of units, and customer C who bought 7 units. In the end, all non-defective units were sold. How many units were sold to Customer B?"""
    # Define the total number of phones and the number of defective phones
    total_phones = 20
    defective_phones = 5

    # Calculate the number of non-defective phones
    non_defective_phones = total_phones - defective_phones

    # Calculate the number of phones sold to customers A and C
    sold_to_a_c = 3 + 7

    # Calculate the number of phones sold to customer B
    sold_to_b = non_defective_phones - sold_to_a_c

    # Return the number of phones sold to customer B
    result = sold_to_b
    return result

print(solution())