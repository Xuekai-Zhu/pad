def solution():
    """Harvey's started out with 25 steaks. Then he sold some, and only had 12 steaks left. He sold 4 more steaks, at 10 dollars. How many steaks did he sell in all?"""
    # Define the initial number of steaks and the final number of steaks
    initial_steaks = 25
    final_steaks = 12

    # Calculate the number of steaks sold
    steaks_sold = initial_steaks - final_steaks

    # Calculate the total sale amount for the 4 additional steaks sold
    additional_sale_amount = 4 * 10

    # Calculate the total number of steaks sold
    total_steaks_sold = steaks_sold + 4

    # Display the total number of steaks sold
    result = total_steaks_sold
    return result

print(solution())