def solution():
    """A store is selling mobile phones. This store contains 20 units of phones but the owner found out that there were 5 defective units. After he got rid of the defective units, he started to sell the rest of his units to customer A who bought 3 units, customer B who bought a certain amount of units, and customer C who bought 7 units. In the end, all non-defective units were sold. How many units were sold to Customer B?"""
    # Define the initial number of units and the number of defective units
    total_units = 20
    defective_units = 5

    # Calculate the number of non-defective units
    non_defective_units = total_units - defective_units

    # Subtract the units sold to customers A and C
    units_sold = 3 + 7
    non_defective_units -= units_sold

    # Calculate the units sold to customer B
    customer_b_units = non_defective_units

    # Display the units sold to customer B
    result = customer_b_units
    return result

print(solution())