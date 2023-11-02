def solution():
    """A party of 4 order 3 dozen oysters on the half shell for $15.00 a dozen, 2 pounds of steamed shrimp for $14.00 a pound and 2 pounds of fried clams for $13.50 a pound. If they split the bill equally, how much will they each owe?"""
    oyster_price = 15
    shrimp_price = 14
    clams_price = 13.5
    oyster_dozen = 3
    shrimp_pounds = 2
    clams_pounds = 2
    total_oyster_price = oyster_price * oyster_dozen
    total_shrimp_price = shrimp_price * shrimp_pounds
    total_clams_price = clams_price * clams_pounds
    total_price = total_oyster_price + total_shrimp_price + total_clams_price
    split_bill = total_price / 4
    result = split_bill
    return result

print(solution())