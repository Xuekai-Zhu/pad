def solution():
    """Juan wants to add croissants to his bakery menu. It takes 1/4 pound of butter to make 1 dozen croissants. He wants to start with making 4 dozen a day for a week. How many pounds of butter will he need to make these croissants?"""
    croissants_per_dozen = 1
    butter_per_dozen = 1/4
    dozens_per_day = 4
    days_per_week = 7
    total_butter = dozens_per_day * butter_per_dozen * days_per_week * croissants_per_dozen
    result = total_butter
    return result

print(solution())