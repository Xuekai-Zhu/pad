def solution():
    bill = 26
    good_tip = bill * 0.20
    gina_tip = bill * 0.05
    diff = good_tip - gina_tip
    result = diff * 100
    return result

print(solution())