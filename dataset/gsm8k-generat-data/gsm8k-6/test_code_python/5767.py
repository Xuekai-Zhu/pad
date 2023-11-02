def solution():
    jefferson_bananas = 56
    walter_bananas = (3/4) * jefferson_bananas  # Walter has 1/4 times fewer bananas than Jefferson
    total_bananas = jefferson_bananas + walter_bananas  # Total number of bananas
    bananas_per_person = total_bananas / 2  # They share the bananas equally
    walter_share = bananas_per_person  # Walter's share of bananas
    result = walter_share
    return result

print(solution())