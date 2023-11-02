def solution():
    # Calculate the total penalty points Jerry has received so far
    penalty_points = 5 * 2 + 10 * 4  # 5 points for interrupting, 10 points for insulting classmates
    remaining_points = 100 - penalty_points  # calculate remaining points before going to the office
    # Calculate how many times Jerry can throw things before reaching 100 points
    throws_allowed = remaining_points // 25
    result = throws_allowed
    return result

print(solution())