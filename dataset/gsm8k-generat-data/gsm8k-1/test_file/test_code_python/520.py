def solution():
    """Jackson is planting tulips. He can fit 6 red tulips in a row and 8 blue tulips in a row. If Jackson buys 36 red tulips and 24 blue tulips, how many rows of flowers will he plant?"""
    red_tulips_per_row = 6
    blue_tulips_per_row = 8
    num_red_tulips = 36
    num_blue_tulips = 24
    num_rows_of_red_tulips = num_red_tulips // red_tulips_per_row
    num_rows_of_blue_tulips = num_blue_tulips // blue_tulips_per_row
    total_num_rows = num_rows_of_red_tulips + num_rows_of_blue_tulips
    result = total_num_rows
    return result

print(solution())