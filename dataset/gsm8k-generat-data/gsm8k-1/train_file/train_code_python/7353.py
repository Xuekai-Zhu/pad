def solution():
    """Helen cuts her lawn starting in March and finishes in October. Her lawn mower uses 2 gallons of gas every 4th time she cuts her lawn. For March, April, September and October, she only cuts her law 2 times per month. In May, June, July and August, she has to cut her lawn 4 times per month. How many gallons of gas will she need to cut her lawn from March through October?"""
    gas_per_cut = 2
    cuts_per_cycle = 4
    march_oct_cuts = 2 * 4  # 2 cuts per month
    may_aug_cuts = 4 * 4  # 4 cuts per month
    total_cuts = march_oct_cuts + may_aug_cuts
    cycles = total_cuts // cuts_per_cycle + 1
    total_gas = cycles * gas_per_cut
    result = total_gas
    return result

print(solution())