def solution():
    # Calculate the amount of coffee John drinks every 4 days
    coffee = 0.5  # 1/2 gallon jugs of cold brew coffee
    cups_per_gallon = 16  # 1 gallon has 16 cups
    cups = coffee * cups_per_gallon
    # Calculate the number of cups of coffee John drinks per day
    cups_per_day = cups / 4
    result = cups_per_day
    return result

print(solution())