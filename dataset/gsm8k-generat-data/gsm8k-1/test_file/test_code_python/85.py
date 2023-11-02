def solution():
    """Christina is planning a birthday party and needs .75 gift bags per invited guest, because 1/4 of attendees don't show up. She invited 16 friends. Gift bags are $2 each. How much will she spend?"""
    invited_guests = 16
    show_up_percent = 75
    gift_bags_per_guest = 0.75
    total_gift_bags = invited_guests * gift_bags_per_guest * (show_up_percent / 100)
    gift_bag_price = 2
    total_price = total_gift_bags * gift_bag_price
    result = total_price
    return result

print(solution())