def solution():
    # Define Brayan's coffee consumption rate and calculate Ivory's rate
    brayan_rate = 4 cups/hour
    ivory_rate = brayan_rate / 2

    # Calculate the total cups of coffee consumed by both in 5 hours
    total_coffee = (brayan_rate + ivory_rate) * 5
    result = total_coffee
    return result

print(solution())