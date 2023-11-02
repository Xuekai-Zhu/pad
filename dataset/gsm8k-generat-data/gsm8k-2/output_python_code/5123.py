def solution():
    """Janet uses her horses' manure as fertilizer. One horse produces 5 gallons of fertilizer per day. Once Janet has collected enough fertilizer, she'll spread it over 20 acres of farmland. Each acre needs 400 gallons of fertilizer and Janet can spread fertilizer over 4 acres per day. If Janet has 80 horses, how long will it take until all her fields are fertilized?"""
    horse_fertilizer = 5
    total_horse_fertilizer = horse_fertilizer * 80
    acres_to_fertilize = 20
    gallons_per_acre = 400
    acres_per_day = 4
    total_gallons_needed = acres_to_fertilize * gallons_per_acre
    days_to_fertilize = total_gallons_needed / (total_horse_fertilizer / acres_per_day)
    result = days_to_fertilize
    return result

print(solution())