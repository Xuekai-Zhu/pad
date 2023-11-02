def solution():
    """Steve wanted to make a total of $100 within four days, so he took on a berry-picking job in Sweden. The job paid $2 for every pound of lingonberries picked. On Monday he picked 8 pounds. Tuesday’s harvest was triple what he had picked the previous day. On Wednesday he felt very tired and decided to rest. How many pounds of lingonberries did Steve have to pick on Thursday?"""
    # Define the target earnings and the earnings from Monday's harvest
    target_earnings = 100
    monday_earnings = 2 * 8

    # Calculate the remaining target earnings after Monday's harvest
    remaining_earnings = target_earnings - monday_earnings

    # Calculate the pounds of lingonberries Steve needs to pick on Thursday
    thursday_pounds = remaining_earnings / (2 * 3**2)

    # Return the result
    result = int(thursday_pounds)
    return result

print(solution())