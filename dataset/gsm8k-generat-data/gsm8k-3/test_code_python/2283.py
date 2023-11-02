def solution():
    """Sebastian plays drums for percussion in an orchestra. He sits next to the brass section where four people play trombone, two play trumpet, and one plays a French horn. In front of them are the strings section with three violinists, a cellist, and a contrabassist. Next to the strings are a trio of clarinets and a quartet of flute players in the woodwinds section. The maestro conducts them all. How many people are in the orchestra?"""
    # Count the number of people in each section
    brass = 4 + 2 + 1
    strings = 3 + 1 + 1
    woodwinds = 3 + 4
    percussion = 1
    maestro = 1

    # Calculate the total number of people in the orchestra
    total = brass + strings + woodwinds + percussion + maestro

    # Display the total number of people
    result = total
    return result

print(solution())