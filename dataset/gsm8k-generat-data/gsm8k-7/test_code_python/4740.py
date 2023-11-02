def solution():
    num_boys = 3
    muffins_per_boy = 12
    num_girls = 2
    muffins_per_girl = 20

    # Calculate the total number of muffins made by the boys
    total_muffins_boys = num_boys * muffins_per_boy

    # Calculate the total number of muffins made by the girls
    total_muffins_girls = num_girls * muffins_per_girl

    # Calculate the total number of muffins for sale
    total_muffins = total_muffins_boys + total_muffins_girls
    result = total_muffins
    return result

print(solution())