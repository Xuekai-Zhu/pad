def solution():
    texts_about_shopping = 5
    texts_asking_why_not_responding = 25  # 5 times more than shopping texts
    proportion_of_text_about_calling_police = 0.1

    # Calculate the total number of shopping and why-not-responding texts
    total_shopping_why_not_responding_texts = texts_about_shopping + texts_asking_why_not_responding

    # Calculate the number of texts about calling the police
    police_texts = int(total_shopping_why_not_responding_texts * proportion_of_text_about_calling_police)

    # Calculate the total number of texts
    total_texts = total_shopping_why_not_responding_texts + police_texts
    result = total_texts
    return result

print(solution())