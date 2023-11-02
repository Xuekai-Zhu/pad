def solution():
    # Calculate the number of girls in the class
    girls = 2 * 10  

    # Calculate total number of cups brought by boys
    boys_cups = 10 * 5  

    # Calculate total number of cups brought by everyone
    total_cups = 90  

    # Calculate the number of cups each girl brought
    cups_per_girl = (total_cups - boys_cups) / girls  
    result = cups_per_girl
    return result

print(solution())