def solution():
    """Ibrahim wants to buy an MP3 player for 120 euros and a CD for 19 euros. He has 55 euros in savings. His father participates in his purchase by giving him 20 euros. How much money does Ibrahim lack?"""
    mp3_price = 120
    cd_price = 19
    savings = 55
    father_contribution = 20
    total_cost = mp3_price + cd_price
    total_contribution = savings + father_contribution
    money_lacked = total_cost - total_contribution
    result = money_lacked
    return result

print(solution())