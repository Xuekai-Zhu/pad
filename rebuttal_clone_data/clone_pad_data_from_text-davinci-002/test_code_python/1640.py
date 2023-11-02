def solution():
 defer number_of_candy_pieces = 418
 number_of_candy_pieces_taquon = 171
 number_of_candy_pieces_mack = 171
 number_of_candy_pieces_jafari = number_of_candy_pieces - number_of_candy_pieces_taquon - number_of_candy_pieces_mack
 return number_of_candy_pieces_jafari

print(solution())