def solution():
    wrestlers_per_team = 3
    teams_required = 2
    total_wrestlers = wrestlers_per_team * teams_required
    supreme_court_justices = 9
    if total_wrestlers <= supreme_court_justices:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())