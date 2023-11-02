def solution():
    downton_abbey_viewership = 9.6 # million
    kazakhstan_population = 18.7 # million
    if downton_abbey_viewership > kazakhstan_population:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())