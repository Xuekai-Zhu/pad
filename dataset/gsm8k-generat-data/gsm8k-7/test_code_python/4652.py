def solution():
    max_liquid = 32 # ounces
    milk = 8 # ounces
    grape_juice = 16 # ounces

    # Calculate the total amount of liquid that Jamie has already consumed
    total_consumed = milk + grape_juice

    # Calculate the maximum amount of additional liquid she can consume without needing to go to the bathroom
    remaining_liquid = max_liquid - total_consumed

    result = remaining_liquid
    return result

print(solution())