def solution():
    """Billy sells DVDs. He has 8 customers on Tuesday. His first 3 customers buy one DVD each. His next 2 customers buy 2 DVDs each. His last 3 customers don't buy any DVDs. How many DVDs did Billy sell on Tuesday?"""
    one_dvd_customers = 3
    two_dvd_customers = 2
    total_dvds = (one_dvd_customers * 1) + (two_dvd_customers * 2)
    result = total_dvds
    return result

print(solution())