def solution():
    # Define lactose intolerance and cream
    lactose_intolerant = True
    cream_contains_milk = True
    # Check if someone with lactose intolerance should avoid cream
    if lactose_intolerant and cream_contains_milk:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())