def solution():
    
    # Define the cost of each suit and dress shirt
    SUIT_COST = 750
    DRESS_SHIRT_COST = 60

    # Define the number of suits and dress pants purchased
    num_suits = 10
    num_dress_pants = 10

    # Calculate the total cost of the suits
    suit_cost = num_suits * SUIT_COST

    # Calculate the total cost of the dress pants
    dress_pant_cost = num_dress_pants * DRESS_SHIRT_COST / 5

    # Calculate the total cost of the dress shirts
    dress_shirt_cost = num_dress_shirts * DRESS_SHIRT_COST

    # Calculate the total cost of everything
    total_cost = suit_cost + dress_pant_cost + dress_shirt_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())