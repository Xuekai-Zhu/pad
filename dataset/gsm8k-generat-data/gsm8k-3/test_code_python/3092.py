def solution():
    """A hardware store sold 10 graphics cards, 14 hard drives, 8 CPUs, and 4 pairs of RAM in one week. The graphics cards cost $600 each, hard drives cost $80 each, CPUs cost $200 each, and RAM cost $60 for each pair. How much money did the store earn this week?"""
    # Define the cost of each hardware component
    GRAPHICS_CARD_PRICE = 600
    HARD_DRIVE_PRICE = 80
    CPU_PRICE = 200
    RAM_PRICE = 60

    # Define the number of each hardware component sold
    graphics_cards_sold = 10
    hard_drives_sold = 14
    cpus_sold = 8
    ram_pairs_sold = 4

    # Calculate the total revenue from graphics cards
    graphics_card_revenue = graphics_cards_sold * GRAPHICS_CARD_PRICE

    # Calculate the total revenue from hard drives
    hard_drive_revenue = hard_drives_sold * HARD_DRIVE_PRICE

    # Calculate the total revenue from CPUs
    cpu_revenue = cpus_sold * CPU_PRICE

    # Calculate the total revenue from RAM
    ram_revenue = ram_pairs_sold * 2 * RAM_PRICE

    # Calculate the total revenue from all hardware sold
    total_revenue = graphics_card_revenue + hard_drive_revenue + cpu_revenue + ram_revenue

    # Display the total revenue
    result = total_revenue
    return result

print(solution())