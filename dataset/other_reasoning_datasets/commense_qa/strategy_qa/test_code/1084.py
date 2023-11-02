def solution():
    # Define the facts about menthol and nicotine
    menthol_addictive = True
    nicotine_addictive = True
    # Check if menthol makes cigarettes less addictive
    if menthol_addictive and nicotine_addictive:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())