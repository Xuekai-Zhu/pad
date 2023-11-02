def solution():
    # Define Sara Paxton's ethnicity and whether she has ancestral ties to Latin America
    sara_ethnicity = ["Irish", "English", "Mexican", "Spanish", "Chilean"]
    has_latin_american_ancestry = "Mexican" in sara_ethnicity
    # Check if Sara Paxton is considered a Latino
    if has_latin_american_ancestry:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())