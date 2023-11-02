def solution():
    num_guests = 12  # 12 guests were invited
    total_money = (num_guests * 5) + 10 + 15  # Samanta collected $5 from each guest, added her own $10, and had $15 leftover
    gift_price = total_money / num_guests  # Divide the total money by the number of guests to get the price of the gift
    result = gift_price
    return result

print(solution())