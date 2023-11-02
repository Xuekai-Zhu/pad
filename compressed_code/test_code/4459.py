def solution():
    
    jefferson_bananas = 56
    walter_bananas = jefferson_bananas - (1/4 * jefferson_bananas)
    total_bananas = jefferson_bananas + walter_bananas
    walter_share = total_bananas / 2
    result = walter_share
    return result

print(solution())