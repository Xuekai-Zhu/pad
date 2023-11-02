def solution():
    snow_white_dwarves = 7
    hobbit_dwarves = 13
    hobbit_warriors = ["Thorin Oakenshield", "Dwalin", "Balin", "Fili", "Kili", "Oin", "Gloin", "Bifur", "Bofur", "Bombur"]
    # Check if Snow White dwarves outnumber Hobbit dwarves and if any of the Hobbit dwarves are warriors
    if snow_white_dwarves > hobbit_dwarves and any(dwarf in hobbit_warriors for dwarf in ["Dwalin", "Balin", "Fili", "Kili", "Thorin Oakenshield"]):
        result = "no"
    else:
        result = "yes"
    return result

print(solution())