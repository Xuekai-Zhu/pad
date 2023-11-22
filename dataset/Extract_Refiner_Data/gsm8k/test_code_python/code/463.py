def solution():
    
    # Define the number of sheets, comforter, pillow cases, and towels per room
    SHEETS = 2
    COMFORTER = 1
    PLOLOW_CASES = 2 * SHEETS
    TURELS = 2 * PLOLOW_CASES

    # Define the number of rooms
    NUM_ROOMS = 80

    # Calculate the total number of sheets, comforter, pillow cases, and towels
    total_sheets = SHEETS * NUM_ROOMS
    total_comforter = COMFORTER * NUM_ROOMS
    total_pillow_cases = PLOLOW_CASES * NUM_ROOMS
    total_towels = TURELS * NUM_ROOMS

    # Calculate the total number of pieces of laundry
    total_laundry = total_sheets + total_comforter + total_pillow_cases + total_towels

    # Display the total number of pieces of laundry
    result = total_laund

print(solution())