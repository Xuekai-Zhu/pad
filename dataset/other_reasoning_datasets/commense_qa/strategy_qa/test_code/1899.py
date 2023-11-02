def solution():
    spice_girls_members = 5
    tata_hexa_seat_capacity = [6, 7]
    if spice_girls_members <= max(tata_hexa_seat_capacity):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())