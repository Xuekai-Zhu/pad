def solution():
    lil_jon_top_song = "Yeah"
    lox_members = ["Styles P", "Sheek Louch", "Jadakiss"]
    collaborators = ["Usher", "Ludacris"]
    lox_collaboration = False
    for collaborator in collaborators:
        for member in lox_members:
            if member in collaborator:
                lox_collaboration = True
    if lox_collaboration:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())