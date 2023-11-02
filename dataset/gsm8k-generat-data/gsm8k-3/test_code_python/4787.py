def solution():
    """In the post-apocalyptic wasteland, 1 lizard is worth 8 bottle caps, 3 lizards are worth 5 gallons of water, and 1 horse is worth 80 gallons of water. Marla can scavenge for 20 bottle caps each day, but needs to pay 4 bottle caps per night for food and shelter. How many days does it take Marla to collect all the bottlecaps she needs to buy a horse?"""
    # Define the exchange rates
    LIZARD_CAPS_EXCHANGE_RATE = 8
    LIZARD_WATER_EXCHANGE_RATE = 3/5
    HORSE_WATER_EXCHANGE_RATE = 80

    # Define Marla's scavenging and living expenses
    DAILY_SCRAPE = 20
    DAILY_EXPENSES = 4

    # Calculate the number of bottle caps Marla needs to buy a horse
    horse_caps = HORSE_WATER_EXCHANGE_RATE * LIZARD_WATER_EXCHANGE_RATE * LIZARD_CAPS_EXCHANGE_RATE

    # Calculate the number of days it will take Marla to earn enough bottle caps
    days = horse_caps / (DAILY_SCRAPE - DAILY_EXPENSES)

    result = days
    return result

print(solution())