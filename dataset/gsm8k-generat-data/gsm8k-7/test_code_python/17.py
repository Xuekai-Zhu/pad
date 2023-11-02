def solution():
    num_pink = 26
    num_green = 15
    num_yellow = 24

    # Carl takes away 4 pink hard hats
    num_pink -= 4

    # John takes away 6 pink hard hats and twice as many green hard hats
    num_pink -= 6
    num_green -= 2*6

    # Calculate the total number of hard hats remaining
    total_num = num_pink + num_green + num_yellow
    result = total_num
    return result

print(solution())