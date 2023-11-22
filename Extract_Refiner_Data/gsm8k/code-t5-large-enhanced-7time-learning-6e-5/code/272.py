def solution():
    
    # Define the initial number of cards
    total_cards = 80

    # Calculate the number of cards with the letter A
    cards_with_A = total_cards * (2/5)

    # Calculate the number of cards remaining after the letter A
    remaining_cards = total_cards - cards_with_A

    # Calculate the number of cards with the letter B
    cards_with_B = remaining_cards * (1/2)

    # Calculate the number of cards remaining after the letter B
    remaining_cards = remaining_cards - cards_with_B

    # Calculate the number of cards with the letter C
    cards_with_C = remaining_cards * (5/8)

    # Calculate the number of cards with the letter D
    cards_with_D = remaining_cards - cards_with_C

    # Display the number of cards with the letter D
    result = cards_with_D
    return result

print(solution())