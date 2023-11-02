def solution():
    initial_dolls = 6  # Peggy has 6 dolls to start with
    grandmother_dolls = 30  # Peggy's grandmother gives her 30 dolls
    additional_dolls = grandmother_dolls / 2  # Peggy receives half of her grandmother's dolls between her birthday and Christmas

    # Calculate Peggy's total number of dolls
    total_dolls = initial_dolls + grandmother_dolls + additional_dolls
    result = total_dolls
    return result

print(solution())