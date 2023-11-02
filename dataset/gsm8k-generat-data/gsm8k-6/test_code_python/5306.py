def solution():
    # Calculate the number of adults at the reunion
    adults = 45 * (1/3) * 3  # one third as many adults as children, multiply by 3 to get actual number of adults
    blue_adults = adults * (1/3)  # one third of adults wore blue
    non_blue_adults = adults - blue_adults  # calculate number of adults who did not wear blue
    result = non_blue_adults
    return result

print(solution())