def solution():
    # Define Angela's kitchen supplies
    angela_pots = 20
    angela_plates = 3 * angela_pots + 6
    angela_cutlery = angela_plates / 2

    # Calculate Sharon's kitchen supplies
    sharon_pots = angela_pots / 2
    sharon_plates = 3 * angela_plates - 20
    sharon_cutlery = 2 * angela_cutlery

    # Calculate the total number of kitchen supplies Sharon wants to buy
    total_supplies = sharon_pots + sharon_plates + sharon_cutlery
    result = total_supplies
    return result

print(solution())