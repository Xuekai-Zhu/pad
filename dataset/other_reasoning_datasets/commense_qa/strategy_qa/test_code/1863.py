def solution():
    # Define the number of pages for Poe's works
    oval_portrait_pages = 2
    pym_novel_pages = 166
    venmurasu_pages = 11159
    
    # Calculate the total number of words in Poe's works using average words per page
    poe_words = (oval_portrait_pages + pym_novel_pages) * 250 + venmurasu_pages * 350
    
    # Calculate the payment for proofreading based on $0.02 per word
    proofreading_rate = 0.02
    proofreading_payment = poe_words * proofreading_rate
    
    # Determine if proofreading Poe's works was lucrative
    if proofreading_payment > 10000:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())