def solution():
    total_tons = 95
    city_a_tons = 16.5
    city_b_tons = 26
    city_c_tons = 24.5
    city_d_tons = total_tons - city_a_tons - city_b_tons - city_c_tons
    result = city_d_tons
    return result

print(solution())