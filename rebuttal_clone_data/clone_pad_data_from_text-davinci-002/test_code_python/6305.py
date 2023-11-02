def solution():
    total_donuts = 40
    donuts_delta = 8
    donuts_beta = 3 * donuts_gamma
    donuts_gamma = total_donuts - donuts_delta - donuts_beta
    result = donuts_gamma
    return result

print(solution())