def solution():
    pictures_per_day = 10  # John takes 10 pictures every day
    days_per_year = 365  # There are 365 days in a year
    years = 3  # John has taken pictures for the past 3 years
    total_pictures = pictures_per_day * days_per_year * years  # Total pictures taken in 3 years

    memory_card_capacity = 50  # Each memory card can store 50 images
    total_memory_cards = total_pictures / memory_card_capacity  # Total memory cards needed
    total_memory_card_cost = total_memory_cards * 60  # Each memory card costs $60

    result = total_memory_card_cost
    return result

print(solution())