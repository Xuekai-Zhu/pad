def solution():
    jimmy_has = 32
    tommy_has = jimmy_has + 10
    ashton_gives = 40
    jimmy_will_have = jimmy_has + ashton_gives
    tommy_will_have = tommy_has + ashton_gives
    difference = tommy_will_have - jimmy_will_have
    result = difference
    return result

print(solution())