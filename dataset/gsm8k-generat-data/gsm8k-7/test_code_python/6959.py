def solution():
    debelyn_dolls = 20
    andrena_dolls = debelyn_dolls - 2

    christel_dolls = 24
    christel_dolls -= 5

    # After the gifts, Andrena has 2 more dolls than Christel
    andrena_dolls = christel_dolls + 2

    # Calculate how many more dolls Andrena has now than Debelyn
    more_dolls = andrena_dolls - debelyn_dolls
    result = more_dolls
    return result

print(solution())