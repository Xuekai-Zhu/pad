def solution():
    oysters = 3
    shrimp = 2
    clams = 2
    oyster_price = 15
    shrimp_price = 14
    clam_price = 13.50
    total_price = (oysters * oyster_price) + (shrimp * shrimp_price) + (clams * clam_price)
    individual_price = total_price / 4
    result = individual_price
    return result

print(solution())