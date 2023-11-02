def solution():
    saltwater_croc_status = "least concern"
    european_otter_status = "near threatened"
    conservation_levels = ["least concern", "near threatened", "vulnerable", "endangered", "critically endangered", "extinct in the wild", "extinct"]
    saltwater_croc_index = conservation_levels.index(saltwater_croc_status)
    european_otter_index = conservation_levels.index(european_otter_status)
    if saltwater_croc_index < european_otter_index:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())