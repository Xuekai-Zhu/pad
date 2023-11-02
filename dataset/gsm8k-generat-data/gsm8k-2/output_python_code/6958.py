def solution():
    """Debelyn, Christel, and Andrena collect dolls. Debelyn had 20 dolls before she gave Andrena 2 dolls. Christel had 24 dolls before giving Andrena 5 dolls. After all the gifts, Andrena now has 2 more dolls than Christel, how many more dolls does Andrena have now than Debelyn?"""
    debelyn_dolls = 20
    andrena_dolls = debelyn_dolls - 2
    christel_dolls = 24 + 5
    andrena_dolls += 2
    
    dolls_difference = andrena_dolls - debelyn_dolls
    result = dolls_difference
    
    return result

print(solution())