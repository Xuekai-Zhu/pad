def solution():
    jefferson_bananas = 56  # Jefferson has 56 bananas
    walter_bananas = jefferson_bananas - (jefferson_bananas * (1/4))  # Walter has 1/4 times fewer bananas than Jefferson
    total_bananas = jefferson_bananas + walter_bananas  # They combine their bananas
    bananas_each = total_bananas / 2  # They share the bananas equally

    # Calculate the number of bananas Walter gets
    walter_gets = bananas_each - (jefferson_bananas * (1/4))
    result = walter_gets
    return result

print(solution())