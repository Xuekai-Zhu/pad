def solution():
    """Martin is casting three bells for the church's belfry. The first bell takes 50 pounds of bronze, the second bell is twice the size of the first bell, and the third bell is four times the size of the second bell. How much bronze does he need total?"""
    first_bell = 50
    second_bell = first_bell * 2
    third_bell = second_bell * 4
    total_bronze = first_bell + second_bell + third_bell
    result = total_bronze
    return result

print(solution())