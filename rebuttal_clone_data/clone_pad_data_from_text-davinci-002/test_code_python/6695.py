def solution():
     pack_price = 5
     individual_price = 1.75
     number_of_lighters = 24
     price_difference = (pack_price * number_of_lighters / 12) - (individual_price * number_of_lighters)
     result = price_difference
     return result

print(solution())