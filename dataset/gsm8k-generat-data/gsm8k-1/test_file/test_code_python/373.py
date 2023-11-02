def solution():
    """Lucy sells apples from her orchard at $4 per piece. On Monday, she sold all the apples picked. On Tuesday, she picked 12 apples. Come Wednesday, Lucy picked double the number of apples she did the previous day. If Lucy got $56 from selling the apples picked on Monday, how many apples did she pick over the three days?"""
    monday_sales = 56
    monday_apples = monday_sales / 4
    tuesday_apples = 12
    wednesday_apples = tuesday_apples * 2
    total_apples = monday_apples + tuesday_apples + wednesday_apples
    result = total_apples
    return result

print(solution())