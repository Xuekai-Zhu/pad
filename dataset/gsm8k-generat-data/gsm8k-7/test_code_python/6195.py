def solution():
    mara_total_crayons = 40
    mara_pink_crayons_percentage = 0.1

    luna_total_crayons = 50
    luna_pink_crayons_percentage = 0.2

    # Calculate the number of pink crayons for Mara and Luna
    mara_pink_crayons = mara_total_crayons * mara_pink_crayons_percentage
    luna_pink_crayons = luna_total_crayons * luna_pink_crayons_percentage

    # Calculate the total number of pink crayons for Mara and Luna
    total_pink_crayons = mara_pink_crayons + luna_pink_crayons
    result = total_pink_crayons
    return result

print(solution())