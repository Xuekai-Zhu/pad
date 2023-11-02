def solution():
    """Sasha made 30 chocolate muffins for her school bake sale fundraiser. Melissa made 4 times as many muffins as Sasha, and Tiffany made half of Sasha and Melissa's total number of muffins. If one muffin sold for $4, how much money did Sasha, Melissa, and Tiffany contribute to the fundraiser?"""
    sasha_muffins = 30
    melissa_muffins = 4 * sasha_muffins
    total_muffins = sasha_muffins + melissa_muffins
    tiffany_muffins = total_muffins / 2
    total_money = (sasha_muffins + melissa_muffins + tiffany_muffins) * 4
    result = total_money
    return result

print(solution())