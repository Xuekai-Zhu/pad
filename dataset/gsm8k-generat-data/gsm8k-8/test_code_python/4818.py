def solution():
    # Define Peggy's starting number of dolls and her grandmother's gift
    peggy_start_dolls = 6
    grandmother_gift = 30

    # Calculate the number of dolls Peggy receives between her birthday and Christmas
    birthday_christmas_dolls = 0.5 * grandmother_gift

    # Add up Peggy's total number of dolls
    total_dolls = peggy_start_dolls + grandmother_gift + birthday_christmas_dolls
    result = total_dolls
    return result

print(solution())