def solution():
    beauty_and_the_beast_collaborators = ["Ron Perlman"]
    sons_of_anarchy_collaborators = ["Kurt Sutter", "Charlie Hunnam", "Ron Perlman"]
    # Check if any of the Beauty and the Beast collaborators were also collaborators with Kurt Sutter
    for collaborator in beauty_and_the_beast_collaborators:
        if collaborator in sons_of_anarchy_collaborators:
            result = "no"
            break
    else:
        result = "yes"
    return result

print(solution())