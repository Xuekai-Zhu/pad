def solution():
    
    # Define the number of red roses Sandra ordered
    red_roses = 4 * red_roses

    # Define the number of pink calla lilies Sandra ordered
    pink_calla_lilies = 200

    # Calculate the number of white carnations Sandra ordered
    white_carnations = red_roses * 5

    # Calculate the total number of red roses ordered
    total_red_roses = red_roses + white_carnations + pink_calla_lilies

    # Calculate the number of red roses Sandra must deliver by 5 pm
    red_roses_delivered = total_red_roses - 5

    # Display the number of red roses Sandra must deliver
    result = red_roses_delivered
    return result

print(solution())