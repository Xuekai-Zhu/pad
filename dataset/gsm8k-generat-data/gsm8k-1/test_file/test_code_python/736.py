def solution():
    """A class of 50 students has various hobbies. 10 like to bake, 5 like to play basketball, and the rest like to either play video games or play music. How many like to play video games if the number that like to play music is twice the number that prefer playing basketball?"""
    total_students = 50
    bake = 10
    basketball = 5
    music = 2 * basketball
    video_games = total_students - (bake + basketball + music)
    result = video_games
    return result

print(solution())