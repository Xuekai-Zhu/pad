def solution():
    
    # Define the number of cards Erica made and the number of cards in each box
    cards_made = 20
    cards_per_box = 15

    # Calculate the total number of cards Erica's dad brought
    dad_cards = 2 * cards_per_box

    # Calculate the total number of cards Erica passed out
    total_given_out = 24 + 5 + 17

    # Calculate the total number of cards Erica has now
    total_cards = cards_made + dad_cards + total_given_out

    # Display the total number of cards Erica has now
    result = total_cards
    return result

print(solution())