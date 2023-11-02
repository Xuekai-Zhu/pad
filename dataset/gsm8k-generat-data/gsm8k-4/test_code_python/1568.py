def solution():
    """Sasha made 30 chocolate muffins for her school bake sale fundraiser. Melissa made 4 times as many muffins as Sasha, and Tiffany made half of Sasha and Melissa's total number of muffins. If one muffin sold for $4, how much money did Sasha, Melissa, and Tiffany contribute to the fundraiser?"""
    # Sasha made 30 muffins
    sasha_muffins = 30

    # Melissa made 4 times as many as Sasha
    melissa_muffins = sasha_muffins * 4

    # Total number of muffins
    total_muffins = sasha_muffins + melissa_muffins

    # Tiffany made half of the total number of muffins
    tiffany_muffins = total_muffins / 2

    # Total money raised from the sale
    total_money_raised = (sasha_muffins + melissa_muffins + tiffany_muffins) * 4

    # return the result
    result = total_money_raised
    return result

print(solution())