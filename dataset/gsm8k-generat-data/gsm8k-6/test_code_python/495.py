def solution():
    # Calculate the total number of snacks
    total_snacks = 64 + 4*64 + 32  # 64 pretzels, four times as many goldfish, and 32 suckers
    snacks_per_baggie = total_snacks / 16  # Divide the total number of snacks by the number of kids

    result = snacks_per_baggie
    return result

print(solution())