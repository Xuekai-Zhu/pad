def solution():
    chocolates_remaining = 24  # Hank gave 24 chocolates to Delphine
    chocolates_eaten = 4  # Delphine ate 4 chocolates on the first day

    # Calculate the number of chocolates eaten on the second day
    chocolates_eaten_second_day = 2*chocolates_eaten - 3
    chocolates_eaten += chocolates_eaten_second_day  # Add the chocolates eaten on the second day to the total

    # Calculate the number of chocolates eaten on the third day
    chocolates_eaten_third_day = chocolates_eaten - 2
    chocolates_eaten += chocolates_eaten_third_day  # Add the chocolates eaten on the third day to the total

    # Calculate the number of chocolates eaten on the fourth day
    chocolates_eaten_fourth_day = chocolates_eaten - 1
    chocolates_eaten += chocolates_eaten_fourth_day  # Add the chocolates eaten on the fourth day to the total

    # Calculate the number of chocolates remaining on the fifth day
    chocolates_remaining = chocolates_remaining - chocolates_eaten
    result = chocolates_remaining
    return result

print(solution())