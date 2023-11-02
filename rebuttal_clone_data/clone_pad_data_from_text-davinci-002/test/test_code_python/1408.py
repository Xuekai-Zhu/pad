def solution():
    total_value = 20000
    earring_value = 6000 * 2
    phone_value = 2000
    scarf_value = 1500
    total_scarf_value = total_value - earring_value - phone_value
    number_of_scarves = total_scarf_value / scarf_value
    result = number_of_scarves
    return result

print(solution())