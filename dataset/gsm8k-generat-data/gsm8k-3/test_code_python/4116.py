def solution():
    """Pierre decides to bring his mother out for ice cream. His treat. Each scoop is $2. If he gets 3 scoops and his mom gets 4, what is the total bill?"""
    # Define the price per scoop of ice cream
    PRICE_PER_SCOOP = 2

    # Define the number of scoops Pierre and his mother each get
    pierre_scoops = 3
    mom_scoops = 4

    # Calculate the total bill
    total_bill = (pierre_scoops + mom_scoops) * PRICE_PER_SCOOP

    # Display the total bill
    result = total_bill
    return result

print(solution())