def solution():
    # Define the minimum requirements to win a Scrabble tournament
    minimum_requirements = {"large vocabulary": True, "reasoning capability": True}
    # Check if a two-year old meets the minimum requirements
    two_year_old = {"limited vocabulary": True, "lacks reasoning capability": True}
    if all(requirement in two_year_old.keys() and two_year_old[requirement] for requirement in minimum_requirements):
        result = "no"
    else:
        result = "yes"
    return result

print(solution())