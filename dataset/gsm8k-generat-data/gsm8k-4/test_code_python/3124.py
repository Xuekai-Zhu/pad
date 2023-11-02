def solution():
    """Nicole has three older sisters. After each one outgrows their clothes, they give them to Nicole. They have all outgrown their clothes and have given them all to Nicole. Nicole started with 10 pieces of clothing. Her first older sister had half as many clothes as Nicole. The next oldest sister had 2 more pieces of clothing than Nicole. The oldest had the average of what her three younger sisters had. How many pieces of clothing does Nicole end up with?"""
    # Nicole starts with 10 pieces of clothing
    nicole_clothes = 10

    # Calculate the number of clothes of the first older sister
    sister1_clothes = nicole_clothes / 2

    # Calculate the number of clothes of the second older sister
    sister2_clothes = nicole_clothes + 2

    # Calculate the average number of clothes of the three younger sisters
    younger_avg_clothes = (nicole_clothes + sister1_clothes + sister2_clothes) / 3

    # Calculate the number of clothes of the oldest sister
    oldest_clothes = younger_avg_clothes

    # Calculate the total number of clothes
    total_clothes = nicole_clothes + sister1_clothes + sister2_clothes + oldest_clothes

    result = total_clothes
    return result

print(solution())