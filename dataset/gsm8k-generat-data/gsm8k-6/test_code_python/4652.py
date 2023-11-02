def solution():
    # Calculate the total amount of liquid Jamie has already consumed
    consumed_liquid = 8 + 16  # 8 ounces of milk and 16 ounces of grape juice
    max_liquid = 32  # The maximum amount of liquid Jamie can have before needing to use the bathroom
    remaining_liquid = max_liquid - consumed_liquid  # the remaining amount of liquid Jamie can drink
    result = remaining_liquid
    return result

print(solution())