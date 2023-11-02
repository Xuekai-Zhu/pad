def solution():
    """Tommy has 10 more sheets than Jimmy does. If Jimmy has 32 sheets, how many more sheets will Jimmy have than Tommy if his friend Ashton gives him 40 sheets."""
    # Define the initial number of sheets for Jimmy and Tommy
    jimmy_sheets = 32
    tommy_sheets = jimmy_sheets + 10

    # Add the sheets given by Ashton to Jimmy's total
    jimmy_sheets += 40

    # Calculate the difference in number of sheets between Jimmy and Tommy
    sheet_difference = jimmy_sheets - tommy_sheets

    # Return the result
    result = sheet_difference
    return result

print(solution())