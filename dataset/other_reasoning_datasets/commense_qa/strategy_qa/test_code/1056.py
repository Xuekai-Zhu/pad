def solution():
    leonardo_birthplace = "Anchiano"
    leonardo_centuries = ["15th", "16th"]
    boticelli_centuries = ["15th", "16th"]
    donatello_centuries = ["15th"]
    boticelli_in_florence = True
    donatello_in_florence = True
    # Check if there were any other Florentine artists that lived and worked in the same centuries as da Vinci
    if (boticelli_in_florence and boticelli_centuries == leonardo_centuries) or (donatello_in_florence and donatello_centuries == leonardo_centuries):
        result = "no"
    else:
        result = "yes"
    return result

print(solution())