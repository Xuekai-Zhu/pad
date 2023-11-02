def solution():
    """Johnny TV makes 25 percent more movies than L&J Productions each year. If  L&J Productions produces 220 movies in a year, how many movies does the two production companies produce in five years combined?"""
    # Define the number of movies produced by L&J Productions in one year
    LJ_YEARLY_MOVIES = 220

    # Calculate the number of movies produced by Johnny TV in one year
    JT_YEARLY_MOVIES = LJ_YEARLY_MOVIES * 1.25

    # Calculate the total number of movies produced by both companies in one year
    TOTAL_YEARLY_MOVIES = LJ_YEARLY_MOVIES + JT_YEARLY_MOVIES

    # Calculate the total number of movies produced by both companies in five years
    TOTAL_FIVE_YEAR_MOVIES = TOTAL_YEARLY_MOVIES * 5

    # Display the total number of movies produced
    result = TOTAL_FIVE_YEAR_MOVIES
    return result

print(solution())