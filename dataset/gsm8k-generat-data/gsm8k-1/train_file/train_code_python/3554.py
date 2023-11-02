def solution():
    """Alex has 4 pens in the first week of a month. Every week her pen collection doubles. How many more pens will Alex have than Jane if Jane will have 16 pens after a month?"""
    alex_pens = 4
    jane_pens = 16
    weeks_in_month = 4
    for i in range(1, weeks_in_month):
        alex_pens *= 2
    difference = alex_pens - jane_pens
    result = difference
    return result

print(solution())