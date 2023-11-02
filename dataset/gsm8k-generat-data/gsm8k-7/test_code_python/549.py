def solution():
    num_chairs = 80
    num_legs_per_chair = 5
    num_tables = 20
    num_legs_per_table = 3
    damaged_chairs_percentage = 0.4

    # Calculate the total number of legs from all chairs
    total_legs_from_chairs = num_chairs * num_legs_per_chair

    # Calculate the total number of legs from all tables
    total_legs_from_tables = num_tables * num_legs_per_table

    # Calculate the number of damaged chairs
    num_damaged_chairs = int(num_chairs * damaged_chairs_percentage)

    # Calculate the total number of legs from undamaged chairs
    total_legs_from_undamaged_chairs = (num_chairs - num_damaged_chairs) * num_legs_per_chair

    # Calculate the total number of legs from all furniture items remaining in the company
    total_remaining_legs = total_legs_from_tables + total_legs_from_undamaged_chairs
    result = total_remaining_legs
    return result

print(solution())