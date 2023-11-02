def solution():
    fred_sheets = 212  # Fred starts with 212 sheets of paper
    jane_sheets = 307  # Jane gives Fred 307 more sheets of paper
    charles_sheets = 156  # Fred gives 156 sheets of paper to Charles

    # Calculate the total number of sheets of paper Fred has left
    total_sheets = fred_sheets + jane_sheets - charles_sheets
    result = total_sheets
    return result

print(solution())