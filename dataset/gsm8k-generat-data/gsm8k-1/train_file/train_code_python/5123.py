def solution():
    """Janet uses her horses' manure as fertilizer. One horse produces 5 gallons of fertilizer per day. Once Janet has collected enough fertilizer, she'll spread it over 20 acres of farmland. Each acre needs 400 gallons of fertilizer and Janet can spread fertilizer over 4 acres per day. If Janet has 80 horses, how long will it take until all her fields are fertilized?"""
    horses = 80
    fertilizer_per_horse = 5
    total_fertilizer = horses * fertilizer_per_horse
    acres_per_day = 4
    gallons_per_acre = 400
    total_gallons_needed = 20 * gallons_per_acre
    days_needed = total_gallons_needed / (total_fertilizer / acres_per_day)
    result = days_needed
    return result

print(solution())