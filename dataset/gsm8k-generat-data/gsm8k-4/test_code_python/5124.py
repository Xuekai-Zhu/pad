def solution():
    """Janet uses her horses' manure as fertilizer. One horse produces 5 gallons of fertilizer per day.
    Once Janet has collected enough fertilizer, she'll spread it over 20 acres of farmland.
    Each acre needs 400 gallons of fertilizer and Janet can spread fertilizer over 4 acres per day.
    If Janet has 80 horses, how long will it take until all her fields are fertilized?"""
    
    # Define the amount of fertilizer produced by one horse in one day
    horse_fertilizer = 5  # in gallons/day
    
    # Define the amount of fertilizer needed for one acre of farmland
    acre_fertilizer = 400  # in gallons
    
    # Define the amount of acres that can be fertilized in one day
    acres_per_day = 4
    
    # Define the total amount of farmland that needs to be fertilized
    total_acres = 20
    
    # Define the total amount of fertilizer needed
    total_fertilizer = total_acres * acre_fertilizer
    
    # Calculate the total amount of fertilizer produced in one day by all the horses combined
    total_horse_fertilizer = 80 * horse_fertilizer  # in gallons/day
    
    # Calculate the number of days it will take to collect enough fertilizer
    days_to_collect = total_fertilizer / total_horse_fertilizer
    
    # Calculate the number of days it will take to spread the fertilizer over all the farmland
    days_to_spread = total_acres / acres_per_day
    
    # Calculate the total number of days
    total_days = days_to_collect + days_to_spread
    
    result = total_days
    return result

print(solution())