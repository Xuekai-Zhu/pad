def solution():
    """240 sixth-grade students were asked about the number of novels they read per month. 
    1/6 of students read three or more novels, 35% of students read two novels, 
    5/12 of students read one novel, and the rest of the students do not read anything. 
    Calculate the number of students who do not read novels."""
    
    # Define the total number of students
    total_students = 240
    
    # Calculate the number of students who read three or more novels
    three_or_more = total_students / 6
    
    # Calculate the number of students who read two novels
    two_novels = total_students * 0.35
    
    # Calculate the number of students who read one novel
    one_novel = total_students * 5/12
    
    # Calculate the total number of students who read novels
    total_readers = three_or_more + two_novels + one_novel
    
    # Calculate the number of students who do not read novels
    non_readers = total_students - total_readers
    
    # Return the result
    result = non_readers
    return result

print(solution())