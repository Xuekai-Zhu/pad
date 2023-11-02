def solution():
    symbol_of_new_baby = "stork"
    baby_shower = True
    if symbol_of_new_baby in ["stork", "baby"] and baby_shower:
        result = "possible"
    else:
        result = "unlikely"
    return result

print(solution())