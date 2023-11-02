def solution():
    pants_cost = 110
    socks_cost = 60
    num_pants = 4
    num_socks = 2
    percent_discount = 30
    pants_total_cost = (pants_cost * num_pants) * (1 - (percent_discount / 100))
    socks_total_cost = (socks_cost * num_socks) * (1 - (percent_discount / 100))
    total_cost = pants_total_cost + socks_total_cost
    result = total_cost
    return result

print(solution())