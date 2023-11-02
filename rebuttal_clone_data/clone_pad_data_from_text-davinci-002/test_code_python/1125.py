def solution():
    Angela_pots = 20
    Angela_plates = Angela_pots * 3 + 6
    Angela_cutlery = Angela_plates / 2
    Sharon_pots = Angela_pots / 2
    Sharon_plates = Angela_plates - 20
    Sharon_cutlery = Angela_cutlery * 2
    result = Sharon_pots + Sharon_plates + Sharon_cutlery
    return result

print(solution())