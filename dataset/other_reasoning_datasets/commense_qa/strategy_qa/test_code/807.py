def solution():
    feline_names = ["Cats", "Tigers", "Lions"]
    baseball_teams = ["River Cats", "Valley Cats", "Flying Tigers"]
    overlap = [team for team in baseball_teams if any(feline_name in team for feline_name in feline_names)]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())