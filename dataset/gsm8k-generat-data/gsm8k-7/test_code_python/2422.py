def solution():
    hershel_betta_fish = 10
    hershel_goldfish = 15
    bexley_betta_fish = (2/5) * hershel_betta_fish
    bexley_goldfish = (1/3) * hershel_goldfish
    hershel_total_fish = hershel_betta_fish + hershel_goldfish
    bexley_total_fish = bexley_betta_fish + bexley_goldfish
    total_fish = hershel_total_fish + bexley_total_fish
    total_gifted_fish = total_fish / 2
    remaining_fish = total_fish - total_gifted_fish
    result = remaining_fish
    return result

print(solution())