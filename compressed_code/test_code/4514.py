def solution():
    
    total_money = 50
    moses_share = total_money * 0.4
    remaining_money = total_money - moses_share
    tony_esther_share = remaining_money / 2
    difference = moses_share - tony_esther_share
    result = difference
    return result

print(solution())