def solution():
    
    angela_pots = 20
    angela_plates = (angela_pots * 3) + 6
    angela_cutlery = angela_plates / 2

    sharon_pots = angela_pots / 2
    sharon_plates = (angela_plates * 3) - 20
    sharon_cutlery = angela_cutlery * 2

    total_supplies = sharon_pots + sharon_plates + sharon_cutlery
    result = total_supplies
    return result

print(solution())