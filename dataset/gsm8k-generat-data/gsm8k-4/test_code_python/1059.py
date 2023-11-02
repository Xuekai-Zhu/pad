def solution():
    """Peyton has 3 children and they each get a juice box in their lunch, 5 days a week.  The school year is 25 weeks long. How many juices boxes will she need for the entire school year for all of her children?"""
    # Define the number of children and the number of days per week they receive juice boxes
    NUM_CHILDREN = 3
    JUICE_BOXES_PER_DAY = NUM_CHILDREN

    # Define the number of weeks in the school year
    NUM_WEEKS = 25

    # Calculate the total number of juice boxes needed for the school year
    total_juice_boxes = NUM_CHILDREN * JUICE_BOXES_PER_DAY * NUM_WEEKS

    result=total_juice_boxes
    return result

print(solution())