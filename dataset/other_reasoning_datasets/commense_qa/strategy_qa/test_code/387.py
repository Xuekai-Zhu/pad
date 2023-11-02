def solution():
    oscar_wilde_famous_book = "The Picture of Dorian Gray"
    eva_green_project = "Penny Dreadful"
    eva_green_character = "Vanessa Ives"
    dorian_gray_appearance = False
    if eva_green_project == "Penny Dreadful" and eva_green_character == "Vanessa Ives":
        dorian_gray_appearance = True
    if dorian_gray_appearance:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())