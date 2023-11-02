def solution():
    ja_rule = "Jeffrey Atkins"
    fifty_cent = "50 Cent"
    if ja_rule.lower() != fifty_cent.lower():
        result = "unknown"
    else:
        result = "no"
    return result

print(solution())