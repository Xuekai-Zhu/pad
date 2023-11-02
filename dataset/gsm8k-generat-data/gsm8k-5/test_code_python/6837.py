def solution():
    # Finding the total number of crayons Annie has
    total_crayons = 21 + 36  # 21 crayons in the pack + 36 in the locker

    # Adding the number of crayons Bobby gave her
    bobby_crayons = 36 / 2
    total_crayons += bobby_crayons

    # Finding the number of crayons Annie gives to Mary
    mary_crayons = total_crayons / 3
    result = mary_crayons
    return result

print(solution())