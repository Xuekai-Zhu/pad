def solution():
    ancient_wonders = ["Great Pyramid of Giza", "Colossus of Rhodes", "Hanging Gardens of Babylon", "Lighthouse of Alexandria", "Mausoleum at Halicarnassus", "Statue of Zeus at Olympia", "Temple of Artemis at Ephesus"]
    intact_wonders = ["Great Pyramid of Giza"]
    destroyed_wonders = ["Colossus of Rhodes", "Hanging Gardens of Babylon", "Lighthouse of Alexandria", "Mausoleum at Halicarnassus", "Statue of Zeus at Olympia"]
    remaining_wonders = [wonder for wonder in ancient_wonders if wonder not in destroyed_wonders]
    if remaining_wonders == intact_wonders:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())