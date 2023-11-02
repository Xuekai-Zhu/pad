def solution():
    """Grandma left $124,600 in her will. She gave half of it to her favorite grandchild, Shelby. The rest was to be evenly divided among the remaining 10 grandchildren. How many dollars did one of the remaining 10 grandchildren receive?"""
    # Calculate how much money Shelby received
    shelby_share = 124600 / 2

    # Calculate how much money was left for the remaining 10 grandchildren
    remaining_money = 124600 - shelby_share

    # Calculate how much money each of the remaining 10 grandchildren received
    each_share = remaining_money / 10

    # Display the amount of money each of the remaining 10 grandchildren received
    result = each_share
    return result

print(solution())