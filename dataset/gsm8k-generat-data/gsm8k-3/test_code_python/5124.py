def solution():
    """Janet uses her horses' manure as fertilizer. One horse produces 5 gallons of fertilizer per day. Once Janet has collected enough fertilizer, she'll spread it over 20 acres of farmland. Each acre needs 400 gallons of fertilizer and Janet can spread fertilizer over 4 acres per day. If Janet has 80 horses, how long will it take until all her fields are fertilized?"""
    # Define the number of horses and the amount of fertilizer produced per horse per day
    NUM_HORSES = 80
    FERTILIZER_PER_HORSE_PER_DAY = 5

    # Calculate the total amount of fertilizer produced per day
    total_fertilizer_per_day = NUM_HORSES * FERTILIZER_PER_HORSE_PER_DAY

    # Calculate the total amount of fertilizer needed for all the acres
    total_fertilizer_needed = 20 * 400

    # Calculate the number of days it will take to collect enough fertilizer
    days_to_collect = total_fertilizer_needed / total_fertilizer_per_day

    # Calculate the number of days it will take to spread the fertilizer
    days_to_spread = 20 / 4

    # Calculate the total number of days it will take to fertilize all the fields
    total_days = days_to_collect + days_to_spread

    # Display the total number of days
    result = total_days
    return result

print(solution())