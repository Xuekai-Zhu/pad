def solution():
    num_pencils_per_day = 10
    num_days = 45
    num_pencils_per_pack = 30
    pencil_pack_cost = 4.0

    # Calculate the total number of pencils Judy will use
    total_pencils = num_pencils_per_day * num_days

    # Calculate the total number of pencil packs needed
    total_packs = total_pencils / num_pencils_per_pack

    # Calculate the total cost of all pencil packs needed
    total_cost = total_packs * pencil_pack_cost
    result = total_cost
    return result

print(solution())