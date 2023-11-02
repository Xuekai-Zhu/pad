def solution():
    # Calculate the number of dolls Debelyn has after giving away 2 dolls
    debelyn_dolls = 20 - 2

    # Calculate the number of dolls Christel has after giving away 5 dolls
    christel_dolls = 24 - 5

    # Calculate the number of dolls Andrena has after receiving the gifts
    andrena_dolls = debelyn_dolls + christel_dolls + 2

    # Calculate the difference between the number of dolls Andrena has and Debelyn has
    difference = andrena_dolls - debelyn_dolls
    result = difference
    return result

print(solution())