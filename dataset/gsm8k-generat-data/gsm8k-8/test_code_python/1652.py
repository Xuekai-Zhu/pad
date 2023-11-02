def solution():
    # Define Jimmy's initial number of sheets
    jimmy_sheets = 32

    # Calculate Tommy's initial number of sheets
    tommy_sheets = jimmy_sheets + 10

    # Calculate the total number of sheets after Ashton gives Jimmy 40
    total_sheets = jimmy_sheets + tommy_sheets + 40

    # Calculate Jimmy's new number of sheets
    jimmy_new_sheets = jimmy_sheets + 40

    # Calculate the difference between Jimmy's and Tommy's new number of sheets
    difference = jimmy_new_sheets - (tommy_sheets + 40)

    result = difference
    return result

print(solution())