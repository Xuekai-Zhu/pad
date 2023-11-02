def solution():
    # Calculate the total amount they spent on playing cards and stickers
    total_spent = 9 + 9 + 10 + 2  # Lola and Dora each contributed $9 for the playing cards and they split the $2 for the stickers evenly

    # Calculate the amount each person spent in total
    amount_spent = total_spent / 2

    # Calculate the cost of the stickers per person
    sticker_cost = (total_spent - 10) / 2  # subtracting the cost of the playing cards from the total amount spent, then dividing by 2 since they split the cost evenly

    # Calculate the number of sticker packs Dora got
    dora_stickers = sticker_cost // 2  # using integer division since the stickers were split evenly
    result = dora_stickers
    return result

print(solution())