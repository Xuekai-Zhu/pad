def solution():
    """Debelyn, Christel, and Andrena collect dolls. Debelyn had 20 dolls before she gave Andrena 2 dolls. Christel had 24 dolls before giving Andrena 5 dolls. After all the gifts, Andrena now has 2 more dolls than Christel, how many more dolls does andrena have now than Debelyn?"""
    debelyn_dolls = 20
    andrena_dolls = debelyn_dolls - 2
    christel_dolls = 24
    christel_dolls_given = 5
    andrena_dolls += christel_dolls_given
    diff = andrena_dolls - debelyn_dolls
    result = diff
    return result

print(solution())