def solution():
    linnaeus_death_year = 1778
    origin_of_species_publish_year = 1859
    did_linnaeus_edit_draft = False
    if linnaeus_death_year < origin_of_species_publish_year:
        did_linnaeus_edit_draft = False
    else:
        did_linnaeus_edit_draft = True
    if did_linnaeus_edit_draft:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())