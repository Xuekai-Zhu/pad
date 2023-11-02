def solution():
    flour_katy = 3 * 5 * 16  # 3 bags of 5 pounds, each pound has 16 ounces
    flour_wendi = 2 * flour_katy
    flour_carrie = flour_wendi - 5 * 16  # 5 pounds less, converted to ounces
    
    difference = flour_carrie - flour_katy  # subtract Katy's flour from Carrie's
    
    # Convert to pounds for easier reading
    result = difference / 16
    return result

print(solution())