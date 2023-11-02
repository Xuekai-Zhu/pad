def solution():
    """A party of 4 order 3 dozen oysters on the half shell for $15.00 a dozen, 2 pounds of steamed shrimp for $14.00 a pound and 2 pounds of fried clams for $13.50 a pound. If they split the bill equally, how much will they each owe?"""
    oyster_price = 15
    shrimp_price = 14
    clams_price = 13.5
    num_oysters = 3 * 12
    num_shrimp = 2
    num_clams = 2
    total_price = (oyster_price * 3 + shrimp_price * num_shrimp + clams_price * num_clams) / 4
    result = total_price
    return result

print(solution())