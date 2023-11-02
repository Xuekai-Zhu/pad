def solution():
    # Calculate the number of muffins Melissa made
    melissa_muffins = 4 * 30

    # Calculate the total number of muffins
    total_muffins = 30 + melissa_muffins

    # Calculate the number of muffins Tiffany made
    tiffany_muffins = 0.5 * total_muffins

    # Calculate the total money contributed to the fundraiser
    total_money = (30 + melissa_muffins + tiffany_muffins) * 4

    result = total_money
    return result

print(solution())