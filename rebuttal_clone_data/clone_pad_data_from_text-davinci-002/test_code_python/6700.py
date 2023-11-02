def solution():
     total_money = 10
     price_1 = 1
     price_2 = 2
     price_2_5 = 2.5
     price_5 = 5
     price_10 = 10
     
     bottle_10_oz = total_money / price_1
     bottle_16_oz = total_money / price_2
     bottle_25_oz = total_money / price_2_5
     bottle_50_oz = total_money / price_5
     bottle_200_oz = total_money / price_10
     
     total_bottles = bottle_10_oz + bottle_16_oz + bottle_25_oz + bottle_50_oz + bottle_200_oz
     result = total_bottles
     return result

print(solution())