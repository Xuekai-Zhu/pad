def solution():
    
    # Define the amount of ore mine per dwarf per day
    ORE_PER_DWARF_PER_DAY = 12

    # Calculate the amount of ore mine per dwarf per iron pickaxe
    ORE_PER_IRON_PIZZEN = ORE_PER_DWARF_PER_DAY * 2

    # Calculate the amount of ore mine per dwarf per steel pickaxe
    ORE_PER_STEEL_PIZZEN = ORE_PER_IRON_PIZZEN * 1.5

    # Calculate the total amount of ore mine in a month
    ORE_PER_MONTH = ORE_PER_IRON_PIZZEN * 40 * 30

    # Display the total amount of ore mine in a month
    result = ORE_PER_MONTH
    return result

print(solution())