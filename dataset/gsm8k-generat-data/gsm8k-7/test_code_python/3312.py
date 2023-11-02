def solution():
    num_main_characters = 5
    num_minor_characters = 4
    minor_character_pay = 15000

    # Calculate the total pay for all minor characters
    total_minor_character_pay = num_minor_characters * minor_character_pay

    # Calculate the pay for one main character (3 times the pay of a minor character)
    main_character_pay = minor_character_pay * 3

    # Calculate the total pay for all main characters
    total_main_character_pay = num_main_characters * main_character_pay

    # Calculate the total pay for all characters per episode
    total_pay = total_minor_character_pay + total_main_character_pay
    result = total_pay
    return result

print(solution())