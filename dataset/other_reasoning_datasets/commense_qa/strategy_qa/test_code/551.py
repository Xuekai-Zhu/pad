def solution():
    # Define the properties of milk and lemon
    milk_acidity = "acidic"
    lemon_acidity = "highly acidic"
    # Check if lemon enhances the flavor of milk
    if milk_acidity == "acidic" and lemon_acidity == "highly acidic":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())