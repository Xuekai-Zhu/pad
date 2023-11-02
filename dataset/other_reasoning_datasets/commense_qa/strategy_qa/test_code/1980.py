def solution():
    play = "Macbeth"
    costumes = ["robes", "pointy hats"]
    helpful_items = ["witches", "spellcasting"]
    overlap = [item for item in helpful_items if item in costumes]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())