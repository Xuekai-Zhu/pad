def solution():
    
    initial_lollipops = 42
    emily_share = initial_lollipops * 2/3
    remaining_lollipops = initial_lollipops - emily_share - 4
    lou_share = remaining_lollipops
    result = lou_share
    return result

print(solution())