def solution():
    """Iris has a berry farm. Her brother and sister help her to pick up the berries and sell them to the market. Iris picked 30 blueberries, her sister picked 20 cranberries, and her brother was able to pick 10 raspberries. If 1/3 of the total berries they were able to pick are rotten and the remaining 1/2 of the fresh berries need to be kept, how many berries will they be able to sell?"""
    # Define the number of berries picked by each person
    iris_berries = 30
    sister_berries = 20
    brother_berries = 10

    # Calculate the total number of berries picked
    total_berries = iris_berries + sister_berries + brother_berries

    # Calculate the number of rotten berries
    rotten_berries = total_berries / 3

    # Calculate the number of fresh berries
    fresh_berries = total_berries - rotten_berries

    # Calculate the number of berries to be kept
    kept_berries = fresh_berries / 2

    # Calculate the number of berries to be sold
    sold_berries = fresh_berries - kept_berries

    # return the result
    result = sold_berries
    return result

print(solution())