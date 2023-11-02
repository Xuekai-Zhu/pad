def solution():
    kitkat = 5
    hersheys = 3 * kitkat
    nerds = 8
    lollipops = 11
    baby_ruths = 10
    reese = baby_ruths / 2
    total_candy = kitkat + hersheys + nerds + lollipops + baby_ruths + reese
    total_candy = total_candy - 5  # Brent gave his little sister 5 lollipops
    result = total_candy
    return result

print(solution())