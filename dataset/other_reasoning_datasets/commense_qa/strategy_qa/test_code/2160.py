def solution():
    british_farthing_obsolete_year = 1960
    hersheys_kisses_red_foil_year = 1962
    # Check if Hershey's Kisses in red foil were sold after the obsoletion of the British farthing
    if hersheys_kisses_red_foil_year > british_farthing_obsolete_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())