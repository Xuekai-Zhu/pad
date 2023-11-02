def solution():
    """A computer factory produces 1500 computers per day. They sell each computer for $150. If they sold 1 week's worth of production, how much money will the company earn?"""
    computers_per_day = 1500
    selling_price_per_computer = 150
    days_in_week = 7
    total_computers = computers_per_day * days_in_week
    total_earnings = total_computers * selling_price_per_computer
    result = total_earnings
    return result

print(solution())