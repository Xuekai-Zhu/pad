def solution():
    """In the post-apocalyptic wasteland, 1 lizard is worth 8 bottle caps, 3 lizards are worth 5 gallons of water, and 1 horse is worth 80 gallons of water. Marla can scavenge for 20 bottle caps each day, but needs to pay 4 bottle caps per night for food and shelter. How many days does it take Marla to collect all the bottlecaps she needs to buy a horse?"""
    # Define the conversion rates
    lizard_to_caps = 8
    lizards_to_water = 3
    water_to_horse = 80

    # Calculate the number of bottle caps needed to buy a horse
    horse_price = water_to_horse / lizards_to_water * lizard_to_caps

    # Calculate the number of bottle caps collected each day
    daily_caps = 20

    # Calculate the number of bottle caps spent each day on food and shelter
    daily_expenses = 4

    # Initialize the number of days and the total number of bottle caps collected
    days = 0
    total_caps = 0

    # Keep collecting bottle caps until enough is collected to buy a horse
    while total_caps < horse_price:
        # Increment the number of days
        days += 1
        
        # Collect bottle caps
        total_caps += daily_caps
        
        # Subtract daily expenses
        total_caps -= daily_expenses

    # Display the number of days it took to collect enough bottle caps
    result = days
    return result

print(solution())