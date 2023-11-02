def solution():
    """An NGO contracted a construction company to build 2000 houses within one year. In the first half of the year, they built the first 3/5 units of the contracted number. Due to unavoidable circumstances, the company could only build an additional 300 units by October. How many units remain from the contracted number that the company is supposed to build?"""
    contracted_units = 2000
    first_half_units = contracted_units * 3/5
    remaining_units = contracted_units - first_half_units - 300
    result = remaining_units
    return result

print(solution())