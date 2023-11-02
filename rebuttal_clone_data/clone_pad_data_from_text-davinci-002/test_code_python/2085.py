def solution():
     SNES_value = 150
     SNES_trade_in_value = SNES_value * 0.8
     NES_trade_in_value = SNES_trade_in_value - 80
     NES_sale_value = NES_trade_in_value + 30
     result = NES_sale_value
     return result

print(solution())