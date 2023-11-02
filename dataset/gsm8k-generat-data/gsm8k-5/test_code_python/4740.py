def solution():
    muffins_per_boy = 12  # Each boy makes 12 muffins
    num_boys = 3  # There are 3 boys
    muffins_from_boys = muffins_per_boy * num_boys  # Total muffins made by the boys

    muffins_per_girl = 20  # Each girl makes 20 muffins
    num_girls = 2  # There are 2 girls
    muffins_from_girls = muffins_per_girl * num_girls  # Total muffins made by the girls

    # Calculate the total number of muffins for sale
    total_muffins = muffins_from_boys + muffins_from_girls
    result = total_muffins
    return result

print(solution())