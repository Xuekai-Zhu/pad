def solution():
    # Set the initial assumption that psychics claim to have special powers
    psychics_claim_special_powers = True
    # Set the assumption that Harry Houdini's wife asked psychics for the code word after his death
    harry_houdinis_wife_asked_psyhics = True
    # Set the assumption that psychics did not know the code word
    psychics_did_not_know_code_word = True
    # Check if Harry Houdini's wife made psychics look foolish by asking for the code word
    if psychics_claim_special_powers and harry_houdinis_wife_asked_psyhics and psychics_did_not_know_code_word:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())