def solution():
    original_dwarf_names = ["Blick", "Flick", "Glick", "Snick", "Plick", "Whick", "Quee"]
    disney_dwarf_names = ["Happy", "Sleepy", "Sneezy", "Grumpy", "Dopey", "Bashful", "Doc"]
    if original_dwarf_names == disney_dwarf_names:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())