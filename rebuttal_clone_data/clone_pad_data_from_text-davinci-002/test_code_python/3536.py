def solution():
    glasses_sold_katya = 8
    glasses_sold_ricky = 9
    glasses_sold_tina = (glasses_sold_katya + glasses_sold_ricky) * 2
    glasses_sold_difference = glasses_sold_tina - glasses_sold_katya
    result = glasses_sold_difference
    return result

print(solution())