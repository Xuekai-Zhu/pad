def solution():
    jefferson_bananas = 56
    walter_bananas = jefferson_bananas - (jefferson_bananas / 4)

    total_bananas = jefferson_bananas + walter_bananas
    bananas_per_person = total_bananas / 2

    walter_gets = bananas_per_person / 2
    result = walter_gets
    return result

print(solution())