def solution():
    num_stone_statues = 10
    stone_statue_price = 20

    num_wooden_statues = 20
    wooden_statue_price = 5

    tax_rate = 0.1

    # Calculate the total earning from stone statues
    stone_statue_earning = num_stone_statues * stone_statue_price

    # Calculate the total earning from wooden statues
    wooden_statue_earning = num_wooden_statues * wooden_statue_price

    # Calculate the total earnings before tax
    total_earning = stone_statue_earning + wooden_statue_earning

    # Calculate the total earnings after tax
    total_earning_after_tax = total_earning * (1 - tax_rate)
    result = total_earning_after_tax
    return result

print(solution())