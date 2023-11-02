def solution():
    pumpkin_price = 3  # The pumpkin patch charges $3 per person for a pumpkin
    revenue = 96  # The pumpkin patch made $96 selling pumpkins for carving
    pumpkins_carved = revenue / pumpkin_price  # Calculate the number of pumpkins carved

    pumpkins_remaining = 83 - pumpkins_carved  # Calculate the number of pumpkins remaining
    cans_of_pie_filling = pumpkins_remaining // 3  # Calculate the number of cans of pie filling
    result = cans_of_pie_filling
    return result

print(solution())