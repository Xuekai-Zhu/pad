def solution():
    """Anna ate 4 apples on Tuesday. On Wednesday, she ate double the apples she ate on Tuesday. 
    On Thursday, Anna ate half the apples she ate on Tuesday. How many apples has Anna eaten by the end of these three days?"""
    tuesday_apples = 4
    wednesday_apples = 2 * tuesday_apples
    thursday_apples = tuesday_apples / 2
    total_apples = tuesday_apples + wednesday_apples + thursday_apples
    result = total_apples
    return result

print(solution())