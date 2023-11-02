def solution():
    # Let's call the ages of the coworkers R, P, T, Ro, and Mi for Roger, Peter, Tom, Robert, and Mike respectively

    # Roger has the same amount of experience as all four of the others combined
    R = P + T + Ro + Mi

    # Roger will retire when he accumulates 50 years of experience
    years_to_retire_R = 50 - R

    # Peter's daughter was 7 years old when he started working and she is now 19
    P_daughter_age_difference = 19 - 7
    P = P_daughter_age_difference

    # Tom has twice as many years of experience as Robert
    T = 2 * (Ro)

    # Robert has 4 years less experience than Peter and 2 more than Mike
    Ro = P - 4
    Mi = P - 6

    # Roger has to work for the remaining number of years until he reaches 50 years of experience
    result = years_to_retire_R
    return result

print(solution())