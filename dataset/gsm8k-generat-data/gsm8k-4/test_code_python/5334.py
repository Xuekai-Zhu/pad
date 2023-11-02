def solution():
    """Judy uses 10 pencils during her 5 day school week. A 30 pack of pencils costs $4. How much will she spend on pencils over 45 days?"""
    # Define the number of pencils used in a week and the cost of a pencil pack
    pencils_per_week = 10
    pencil_pack_cost = 4

    # Calculate the number of weeks in 45 days
    num_weeks = 45 / 7

    # Calculate the total number of pencils used over 45 days
    total_pencils = pencils_per_week * num_weeks

    # Calculate the total number of pencil packs needed
    total_packs = total_pencils / 30

    # Calculate the total cost of the pencil packs
    total_cost = total_packs * pencil_pack_cost

    # return the result
    result = total_cost
    return result

print(solution())