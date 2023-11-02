def solution():
    # Define the variables
    cards_transcribed = 200
    card_payment = 0.70
    bonus_threshold = 100
    bonus_payment = 10

    # Calculate the total payment for transcribing cards
    card_total_payment = cards_transcribed * card_payment

    # Calculate the number of bonuses earned
    bonuses_earned = cards_transcribed // bonus_threshold

    # Calculate the total payment for bonuses earned
    bonus_total_payment = bonuses_earned * bonus_payment

    # Calculate the overall total payment
    overall_payment = card_total_payment + bonus_total_payment
    result = overall_payment
    return result

print(solution())