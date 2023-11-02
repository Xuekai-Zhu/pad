def solution():
    """Mr Castiel prepared 600 boar sausages on the weekend. He ate 2/5 of them on Monday, half of the remaining on Tuesday and saved the rest for Friday. If he ate 3/4 of the remaining boar sausages on Friday, how many sausages are left?"""
    # Define the number of sausages prepared
    sausages_prepared = 600

    # Calculate the number of sausages eaten on Monday
    sausages_eaten_monday = sausages_prepared * 2/5

    # Calculate the number of sausages remaining after Monday
    sausages_remaining_tuesday = sausages_prepared - sausages_eaten_monday

    # Calculate the number of sausages eaten on Tuesday
    sausages_eaten_tuesday = sausages_remaining_tuesday * 1/2

    # Calculate the number of sausages remaining after Tuesday
    sausages_remaining_friday = sausages_remaining_tuesday - sausages_eaten_tuesday

    # Calculate the number of sausages eaten on Friday
    sausages_eaten_friday = sausages_remaining_friday * 3/4

    # Calculate the number of sausages remaining after Friday
    sausages_remaining = sausages_remaining_friday - sausages_eaten_friday

    # Display the number of sausages remaining
    result = sausages_remaining
    return result

print(solution())