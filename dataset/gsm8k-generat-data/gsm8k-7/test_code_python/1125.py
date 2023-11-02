def solution():
    angela_pots = 20
    angela_plates = 3 * angela_pots + 6
    angela_cutlery = angela_plates / 2

    sharon_pots = angela_pots / 2
    sharon_plates = 3 * angela_plates - 20
    sharon_cutlery = 2 * angela_cutlery

    total_supplies = sharon_pots + sharon_plates + sharon_cutlery
    result = total_supplies
    return result

print(solution())