def solution():
    """Melody needs to read 20 pages for her English class, 16 pages for her Science class, 8 pages for her Civics, and 12 pages for her Chinese class. She decided to read one-fourth of the number of pages for each class tomorrow. How many pages will she read tomorrow?"""
    # Define the number of pages for each class
    ENG_PAGES = 20
    SCI_PAGES = 16
    CIV_PAGES = 8
    CHI_PAGES = 12

    # Calculate the number of pages Melody will read tomorrow for each class
    eng_pages_tmrw = ENG_PAGES / 4
    sci_pages_tmrw = SCI_PAGES / 4
    civ_pages_tmrw = CIV_PAGES / 4
    chi_pages_tmrw = CHI_PAGES / 4

    # Calculate the total number of pages Melody will read tomorrow
    total_pages_tmrw = eng_pages_tmrw + sci_pages_tmrw + civ_pages_tmrw + chi_pages_tmrw
    result = total_pages_tmrw
    return result

print(solution())