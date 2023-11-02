def solution():
    """
    A store is selling mobile phones. This store contains 20 units of phones but the owner found out that there were 5 defective units.
    After he got rid of the defective units, he started to sell the rest of his units to customer A who bought 3 units,
    customer B who bought a certain amount of units, and customer C who bought 7 units.
    In the end, all non-defective units were sold. How many units were sold to Customer B?
    """
    total_units = 20
    defective_units = 5
    non_defective_units = total_units - defective_units
    non_defective_units_sold = 3 + 7
    customer_b_units_sold = non_defective_units - non_defective_units_sold
    result = customer_b_units_sold
    return result

print(solution())