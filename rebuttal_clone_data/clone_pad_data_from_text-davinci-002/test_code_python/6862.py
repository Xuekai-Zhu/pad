def solution():
     total_attendees = 500
     percent_for_band = 70
     ticket_price = 30
     total_money = total_attendees * ticket_price
     money_for_band = total_money * (percent_for_band / 100)
     band_members = 4
     money_per_band_member = money_for_band / band_members
     result = money_per_band_member
     return result

print(solution())