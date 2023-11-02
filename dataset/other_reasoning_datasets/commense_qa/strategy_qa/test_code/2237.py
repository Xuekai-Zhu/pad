def solution():
    # Aldi cuts costs through various methods
    costs_cutting_methods = ["charge for bags", "buy in bulk", "avoid brand name items"]
    # Aldi removes spoiled or expired foods immediately
    food_handling_methods = ["remove expired food immediately"]
    # Check if Aldi discounts food due to being out of date
    if "remove expired food immediately" in food_handling_methods:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())