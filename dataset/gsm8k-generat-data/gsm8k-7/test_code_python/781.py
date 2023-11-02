def solution():
    cd1_price = 100
    cd2_price = 50
    cd3_price = 85
    num_cds_per_type = 3

    # Calculate the total cost of 3 CDs of type 1
    total_cd1_cost = cd1_price * num_cds_per_type

    # Calculate the total cost of 3 CDs of type 2
    total_cd2_cost = cd2_price * num_cds_per_type

    # Calculate the total cost of 3 CDs of type 3
    total_cd3_cost = cd3_price * num_cds_per_type

    # Calculate the total cost of all CDs
    total_cost = total_cd1_cost + total_cd2_cost + total_cd3_cost
    result = total_cost
    return result

print(solution())