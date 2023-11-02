def solution():
    # Find the number of muffins made by Melissa and Tiffany
    muffins_Melissa = 4 * 30  # Melissa made 4 times as many muffins as Sasha
    muffins_Tiffany = (1/2) * (30 + muffins_Melissa)  # Tiffany made half of Sasha and Melissa's total number of muffins

    # Calculate the total money contributed by Sasha, Melissa, and Tiffany
    total_money = 30 + muffins_Melissa + muffins_Tiffany  # total number of muffins sold
    total_money *= 4  # each muffin sold for $4
    result = total_money
    return result

print(solution())