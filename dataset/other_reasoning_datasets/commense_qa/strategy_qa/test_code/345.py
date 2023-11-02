def solution():
    # Define the method of production for Twinkies
    production_method = "machine-made"
    # Check if Twinkies are considered artisan-made
    if production_method == "machine-made":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())