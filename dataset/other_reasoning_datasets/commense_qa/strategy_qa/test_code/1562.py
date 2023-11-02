def solution():
    beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"]
    george_harrison_spouse = "Pattie Boyd"
    eric_clapton_spouse = "Pattie Boyd"
    for member in beatles:
        if member != "George Harrison" and member in eric_clapton_spouse:
            result = "yes"
            break
        else:
            result = "no"
    return result

print(solution())