def solution():
    """A plant supplier was able to sell 20 pieces of orchids for $50 each and 15 pieces potted Chinese money plant for $25. The money he earned was then used to pay his two workers $40 each and to buy new pots worth $150. How much money was left from the plant supplier's earnings?"""
    # Define the prices and quantities of orchids and Chinese money plants
    orchids_price = 50
    orchids_quantity = 20
    CMP_price = 25
    CMP_quantity = 15

    # Calculate the total earnings from selling orchids and Chinese money plants
    total_earnings = (orchids_price * orchids_quantity) + (CMP_price * CMP_quantity)

    # Calculate the total cost of paying the workers and buying new pots
    total_cost = (2 * 40) + 150

    # Calculate the remaining earnings
    remaining_earnings = total_earnings - total_cost

    # return the result
    result = remaining_earnings
    return result

print(solution())