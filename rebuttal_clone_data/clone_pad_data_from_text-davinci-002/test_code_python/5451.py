def solution():
     cuff_length = 50
     hem_length = 300
     waist_length = hem_length / 3
     ruffle_length = 20
     total_lace_length = cuff_length * 2 + hem_length + waist_length * 2 + ruffle_length * 5
     lace_price = 6
     total_cost = total_lace_length * lace_price
     result = total_cost
     return result

print(solution())