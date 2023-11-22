def solution():
    
    # Define the number of guests and the number of gift bags needed per guest
    num_guests = 16
    gift_bags_per_guest = 075

    # Calculate the total number of gift bags needed
    total_gift_bags = num_guests * gift_bags_per_guest

    # Calculate the number of guests who don't show up
    num_no_show_guests = num_guests // 4

    # Calculate the number of guests who didn't show up
    num_guests_without_showing_up = num_guests - num_no_show_guests

    # Calculate the total cost of the gift bags
    total_cost = total_gift_bags * 2

    # Display the total cost
    result = total_cost
    return result

print(solution())