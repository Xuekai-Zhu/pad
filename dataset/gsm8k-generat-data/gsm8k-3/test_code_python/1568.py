def solution():
    """Sasha made 30 chocolate muffins for her school bake sale fundraiser. 
    Melissa made 4 times as many muffins as Sasha, and Tiffany made half of 
    Sasha and Melissa's total number of muffins. If one muffin sold for $4, 
    how much money did Sasha, Melissa, and Tiffany contribute to the fundraiser?"""
    
    # Define the number of muffins each person made
    sasha_muffins = 30
    melissa_muffins = 4 * sasha_muffins
    total_muffins = sasha_muffins + melissa_muffins
    tiffany_muffins = total_muffins / 2
    
    # Calculate the total amount of money raised for the fundraiser
    total_money = (sasha_muffins + melissa_muffins + tiffany_muffins) * 4
    
    # Calculate the amount of money each person contributed to the fundraiser
    sasha_money = sasha_muffins * 4
    melissa_money = melissa_muffins * 4
    tiffany_money = tiffany_muffins * 4
    
    # Display the amount of money each person contributed to the fundraiser
    result = f"Sasha contributed ${sasha_money:.2f}, Melissa contributed ${melissa_money:.2f}, and Tiffany contributed ${tiffany_money:.2f}."
    return result

print(solution())