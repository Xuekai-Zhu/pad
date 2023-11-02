def solution():
    honey_badger_anatomy = ["anal sacs"]
    hyena_anatomy = ["anal sacs"]
    if set(honey_badger_anatomy) == set(hyena_anatomy):
        result = "no"
    else:
        result = "yes"
    return result

print(solution())