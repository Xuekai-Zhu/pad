def solution():
    """Tommy has 10 more sheets than Jimmy does. If Jimmy has 32 sheets, how many more sheets will Jimmy have than Tommy if his friend Ashton gives him 40 sheets."""
    jimmy_sheets = 32
    tommy_sheets = jimmy_sheets + 10
    ashton_sheets = 40
    jimmy_sheets += ashton_sheets
    difference = jimmy_sheets - tommy_sheets
    result = difference
    return result

print(solution())