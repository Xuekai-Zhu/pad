def solution():
    """An NGO contracted a construction company to build 2000 houses within one year. In the first half of the year, they built the first 3/5 units of the contracted number. Due to unavoidable circumstances, the company could only build an additional 300 units by October. How many units remain from the contracted number that the company is supposed to build?"""
    # Define the total number of houses to be built
    total_houses = 2000

    # Calculate the number of houses built in the first half of the year
    houses_built_first_half = total_houses * (3/5)

    # Calculate the number of houses built by October
    houses_built_by_october = houses_built_first_half + 300

    # Calculate the number of houses remaining to be built
    houses_remaining = total_houses - houses_built_by_october

    result = houses_remaining
    return result

print(solution())