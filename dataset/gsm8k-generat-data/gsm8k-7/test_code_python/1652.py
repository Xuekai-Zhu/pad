def solution():
    jimmy_sheets = 32
    tommy_sheets = jimmy_sheets + 10
    ashton_sheets = 40

    # Add the sheets Ashton gives to Jimmy's total
    jimmy_sheets += ashton_sheets

    # Calculate the difference between Jimmy and Tommy's sheets
    diff_sheets = jimmy_sheets - tommy_sheets
    result = diff_sheets
    return result

print(solution())