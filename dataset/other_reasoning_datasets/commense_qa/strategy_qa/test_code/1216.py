def solution():
    lion_king_characters = ["Simba", "Nala", "Timon", "Pumbaa"]
    warthog_on_broadway = "Pumbaa" in lion_king_characters
    if warthog_on_broadway:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())