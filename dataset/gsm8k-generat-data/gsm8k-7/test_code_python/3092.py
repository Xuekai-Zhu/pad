def solution():
    num_graphics_cards = 10
    graphics_card_price = 600

    num_hard_drives = 14
    hard_drive_price = 80

    num_cpus = 8
    cpu_price = 200

    num_ram_pairs = 4
    ram_pair_price = 60

    # Calculate the total revenue from graphics cards
    graphics_card_revenue = num_graphics_cards * graphics_card_price

    # Calculate the total revenue from hard drives
    hard_drive_revenue = num_hard_drives * hard_drive_price

    # Calculate the total revenue from CPUs
    cpu_revenue = num_cpus * cpu_price

    # Calculate the total revenue from RAM
    ram_revenue = num_ram_pairs * ram_pair_price

    # Calculate the total revenue earned by the store
    total_revenue = graphics_card_revenue + hard_drive_revenue + cpu_revenue + ram_revenue
    result = total_revenue
    return result

print(solution())