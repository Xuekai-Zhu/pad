def solution():
    """Lennon is a sales rep and is paid $0.36 in mileage reimbursement when he travels to meet with clients. On Monday he drove 18 miles. Tuesday he drove 26 miles. Wednesday and Thursday he drove 20 miles each day and on Friday he drove 16 miles. How much money will he be reimbursed?"""
    total_mileage = 18 + 26 + 20 + 20 + 16
    reimburse_rate = 0.36
    total_reimbursement = total_mileage * reimburse_rate
    result = total_reimbursement
    return result

print(solution())