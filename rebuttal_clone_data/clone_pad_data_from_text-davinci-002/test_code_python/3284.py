def solution():
     total_coins = 10
     total_value = 11
     loonie_value = 1
     toonie_value = 2
     toonies = (total_value - (total_coins * loonie_value)) / toonie_value
     result = toonies
     return result

print(solution())