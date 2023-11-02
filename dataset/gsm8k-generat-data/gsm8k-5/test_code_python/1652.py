def solution():
    jimmy_sheets = 32  # Jimmy has 32 sheets
    tommy_sheets = jimmy_sheets + 10  # Tommy has 10 more sheets than Jimmy
    ashton_sheets = 40  # Ashton gives Jimmy 40 sheets

    # Calculate the total number of sheets Jimmy will have after getting the sheets from Ashton
    total_jimmy_sheets = jimmy_sheets + ashton_sheets

    # Calculate the total number of sheets Tommy will have after Jimmy gets the sheets from Ashton
    total_tommy_sheets = tommy_sheets + ashton_sheets

    # Calculate the difference in the number of sheets between Jimmy and Tommy
    difference_sheets = total_jimmy_sheets - total_tommy_sheets
    result = difference_sheets
    return result

print(solution())