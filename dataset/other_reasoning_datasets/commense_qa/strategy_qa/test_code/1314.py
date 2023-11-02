def solution():
    jack_heavyweight_defenses = 5
    klitschko_heavyweight_wins = 25
    jack_lightheavyweight_title_holder = False
    michalczewski_lightheavyweight_wins = 23
    if jack_heavyweight_defenses > klitschko_heavyweight_wins or not jack_lightheavyweight_title_holder:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())