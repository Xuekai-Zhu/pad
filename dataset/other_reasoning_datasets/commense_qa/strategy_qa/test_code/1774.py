def solution():
    # Create a list of Disney princesses
    disney_princesses = ["Snow White", "Cinderella", "Aurora", "Ariel", "Belle", "Jasmine", "Pocahontas", "Mulan", "Tiana", "Rapunzel", "Merida", "Moana"]
    # Check if Elsa is in the list of Disney princesses
    if "Elsa" in disney_princesses:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())