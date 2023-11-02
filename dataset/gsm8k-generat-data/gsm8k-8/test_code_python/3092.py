def solution():
    # Calculate the total earnings from graphics cards
    graphics_cards_earnings = 10 * 600

    # Calculate the total earnings from hard drives
    hard_drives_earnings = 14 * 80

    # Calculate the total earnings from CPUs
    cpus_earnings = 8 * 200

    # Calculate the total earnings from RAM
    ram_earnings = 4 * 60

    # Calculate the total earnings for the week
    total_earnings = graphics_cards_earnings + hard_drives_earnings + cpus_earnings + ram_earnings
    result = total_earnings
    return result

print(solution())