def solution():
    ratio = 2:1:3
    money_amy = 50
    money_ruth = money_amy * (ratio[2] / ratio[1])
    money_sam = money_amy + money_ruth
    money_sandra = money_sam / ratio[0]
    result = money_sandra
    
    return result

print(solution())