def solution():
    kitkats = 5
    hersheys = 3 * kitkats
    nerds = 8
    lollipops = 11
    baby_ruths = 10
    reeses = baby_ruths / 2
    total_candy = kitkats + hersheys + nerds + lollipops + baby_ruths + reeses
    candy_given_away = 5
    total_candy_left = total_candy - candy_given_away
    result = total_candy_left
    return result

print(solution())