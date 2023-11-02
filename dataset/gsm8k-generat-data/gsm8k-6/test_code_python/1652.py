def solution():
    # Find Tommy's number of sheets
    jimmy_sheets = 32
    tommy_sheets = jimmy_sheets + 10

    # Calculate the new number of sheets for Jimmy after Ashton gives him 40
    jimmy_sheets += 40

    # Calculate the difference in sheets between Jimmy and Tommy
    difference = jimmy_sheets - tommy_sheets
    result = difference
    return result

print(solution())