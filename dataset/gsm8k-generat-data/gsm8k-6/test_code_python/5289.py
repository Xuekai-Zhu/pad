def solution():
    # Calculate the total weight of papers not delivered in 10 weeks
    papers_weight = ((6*8*250) + (1*16*250)) * 10  # Monday-Saturday papers weigh 8 ounces each and Sunday paper weighs 16 ounces
    # Convert paper weight to tons and multiply by recycling price per ton to get the total amount made
    total_cash = (papers_weight/32000) * 20  # 1 ton = 32000 ounces
    result = total_cash
    return result

print(solution())