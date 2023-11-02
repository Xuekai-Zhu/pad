def solution():
    """For her 30th birthday, Elvira chose a new computer with many accessories as a gift. She has a budget of €1500 donated by her whole family and thinks that she will be able to keep a little money to afford a garment. She goes to a computer store and chooses a machine that costs €1090 with a screen, keyboard and mouse. She also takes a scanner for €157, a CD burner worth €74 and a printer for €102. How much money will she have left for her clothing?"""
    budget = 1500
    total_cost = 1090 + 157 + 74 + 102
    leftover_money = budget - total_cost
    result = leftover_money
    return result

print(solution())