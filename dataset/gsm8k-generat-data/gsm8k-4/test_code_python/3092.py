def solution():
    """A hardware store sold 10 graphics cards, 14 hard drives, 8 CPUs, and 4 pairs of RAM in one week. The graphics cards cost $600 each, hard drives cost $80 each, CPUs cost $200 each, and RAM cost $60 for each pair. How much money did the store earn this week?"""
    # Define the prices of each item
    graphics_card_price = 600
    hard_drive_price = 80
    cpu_price = 200
    ram_price = 60

    # Calculate the total earnings from selling graphics cards
    graphics_card_earnings = 10 * graphics_card_price

    # Calculate the total earnings from selling hard drives
    hard_drive_earnings = 14 * hard_drive_price

    # Calculate the total earnings from selling CPUs
    cpu_earnings = 8 * cpu_price

    # Calculate the total earnings from selling RAM
    ram_earnings = 4 * (ram_price / 2)

    # Calculate the total earnings for the week
    total_earnings = graphics_card_earnings + hard_drive_earnings + cpu_earnings + ram_earnings

    # return the result
    result = total_earnings
    return result

print(solution())