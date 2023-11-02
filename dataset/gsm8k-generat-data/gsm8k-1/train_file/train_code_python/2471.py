def solution():
    """Karen packs peanut butter sandwiches in her daughter's lunch 2 randomly chosen days of the week. The other 3 school days, she packs a ham sandwich. She packs a piece of cake on one randomly chosen day and cookies the other four days. What is the probability, expressed as a percentage, that Karen packs a ham sandwich and cake on the same day?"""
    pb_days = 2
    ham_days = 3
    cake_days = 1
    cookie_days = 4
    total_days = pb_days + ham_days + cake_days + cookie_days
    ham_and_cake_days = 1
    probability = (ham_days/total_days) * (ham_and_cake_days/ham_days) * 100
    result = probability
    return result

print(solution())