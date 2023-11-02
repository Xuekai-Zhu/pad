def solution():
    """Today Geoff bought 2 pairs of sneakers and spent $60 equally between the two. Tomorrow, he's going to spend 4 times as much on sneakers than he did on Monday. Wednesday, he'll spend 5 times as much on sneakers than he did on Monday. How much will Geoff spend on sneakers over these three days?"""
    monday_spending = 30 # ($60 divided by 2 pairs of sneakers)
    tuesday_spending = monday_spending * 4
    wednesday_spending = monday_spending * 5
    total_spending = monday_spending + tuesday_spending + wednesday_spending
    result = total_spending
    return result

print(solution())