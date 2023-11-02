def solution():
    is_koala_herbivore = True
    koala_dietary_staple = "eucalyptus"
    does_koala_prefer_meat = False
    if is_koala_herbivore and koala_dietary_staple == "eucalyptus" and not does_koala_prefer_meat:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())