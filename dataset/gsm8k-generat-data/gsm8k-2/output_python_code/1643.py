def solution():
    """John has taken 10 pictures every day for the past 3 years. He saves them in raw format so each memory card can store 50 images. Each memory card costs $60. How much does he spend on memory cards?"""
    pictures_per_day = 10
    days_per_year = 365
    years = 3
    total_pictures = pictures_per_day * days_per_year * years
    cards_needed = (total_pictures // 50) + 1  # add 1 to round up to the nearest card
    card_cost = 60
    total_cost = cards_needed * card_cost
    result = total_cost
    return result

print(solution())