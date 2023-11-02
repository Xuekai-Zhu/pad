def solution():
    # Calculate the total earnings from selling graphics cards
    graphics_cards_earnings = 10 * 600

    # Calculate the total earnings from selling hard drives
    hard_drives_earnings = 14 * 80

    # Calculate the total earnings from selling CPUs
    CPUs_earnings = 8 * 200

    # Calculate the total earnings from selling RAM
    RAM_earnings = 4 * 60

    # Calculate the total earnings from selling all items
    total_earnings = graphics_cards_earnings + hard_drives_earnings + CPUs_earnings + RAM_earnings
    result = total_earnings
    return result

print(solution())