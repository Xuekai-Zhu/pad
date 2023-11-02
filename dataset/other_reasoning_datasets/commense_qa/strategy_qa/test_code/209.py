def solution():
    gray_seal_range = "parts of the northern hemisphere bordered by the Atlantic ocean"
    sperm_whale_distribution = "north Atlantic and most other bodies of water on earth"
    if gray_seal_range in sperm_whale_distribution:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())