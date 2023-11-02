def solution():
    """Sebastian plays drums for percussion in an orchestra. He sits next to the brass section where four people play trombone, two play trumpet, and one plays a French horn. In front of them are the strings section with three violinists, a cellist, and a contrabassist. Next to the strings are a trio of clarinets and a quartet of flute players in the woodwinds section. The maestro conducts them all. How many people are in the orchestra?"""
    # Define the number of people in each section
    percussion = 1
    brass = 4 + 2 + 1
    strings = 3 + 1 + 1
    woodwinds = 3 + 4
    maestro = 1

    # Calculate the total number of people in the orchestra
    total_people = percussion + brass + strings + woodwinds + maestro

    # return the result
    result = total_people
    return result

print(solution())