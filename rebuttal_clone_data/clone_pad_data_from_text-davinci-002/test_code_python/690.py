def solution():
     imported_wine = 2400
     domestic_wine = imported_wine / 2
     total_wine = imported_wine + domestic_wine
     bottles_consumed = 1/3 * total_wine
     bottles_remaining = total_wine - bottles_consumed
     result = bottles_remaining
     return result

print(solution())