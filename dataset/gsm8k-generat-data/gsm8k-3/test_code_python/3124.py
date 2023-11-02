def solution():
    """Nicole has three older sisters. After each one outgrows their clothes, they give them to Nicole. They have all outgrown their clothes and have given them all to Nicole. Nicole started with 10 pieces of clothing. Her first older sister had half as many clothes as Nicole. The next oldest sister had 2 more pieces of clothing than Nicole. The oldest had the average of what her three younger sisters had. How many pieces of clothing does Nicole end up with?"""
    # Nicole starts with 10 pieces of clothing
    nicole_clothes = 10

    # Her first older sister had half as many clothes as Nicole
    sister1_clothes = int(nicole_clothes / 2)

    # The next oldest sister had 2 more pieces of clothing than Nicole
    sister2_clothes = nicole_clothes + 2

    # The oldest had the average of what her three younger sisters had
    total_clothes = nicole_clothes + sister1_clothes + sister2_clothes
    sister3_clothes = int(total_clothes / 4)

    # Calculate the total number of clothes Nicole ends up with
    total_clothes += sister3_clothes

    # Display the total number of clothes
    result = total_clothes
    return result

print(solution())