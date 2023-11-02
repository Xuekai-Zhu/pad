def solution():
    cpu_chip_size = 1 #inch
    housekey_size = 0.5 #inch
    if cpu_chip_size < housekey_size:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())