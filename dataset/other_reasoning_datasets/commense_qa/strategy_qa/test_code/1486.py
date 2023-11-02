def solution():
    spartans = 300
    thespians = 700
    persians = 150000
    mozart_compositions = 600
    total_army_size = spartans + thespians
    if total_army_size > mozart_compositions and total_army_size < persians:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())