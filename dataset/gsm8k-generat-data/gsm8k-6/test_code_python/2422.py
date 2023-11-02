def solution():
    hershel_betta = 10
    hershel_goldfish = 15
    bexley_betta = (2/5) * hershel_betta
    bexley_goldfish = (1/3) * hershel_goldfish
    total_betta = hershel_betta + bexley_betta
    total_goldfish = hershel_goldfish + bexley_goldfish
    total_fish = total_betta + total_goldfish
    hershel_gift = total_fish / 2
    remaining_fish = total_fish - hershel_gift
    result = remaining_fish
    return result

print(solution())