def solution():
    candles_blowing = True
    birthday_celebration = True
    funeral = False # assume it's a funeral since cakes are not served there
    if candles_blowing and birthday_celebration and not funeral:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())