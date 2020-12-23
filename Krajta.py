
import tkinter as tk
root = tk.Tk()
size_of_field = 75
canvas = tk.Canvas(bg="#7cbfbc", width = size_of_field * 10, height = size_of_field * 10)
canvas.pack()

class Coords:               #Coords IDs 1 - 16
    _8 = canvas.create_text(0.5 * size_of_field, 1.5 * size_of_field, text = "8", font = 30)
    _7 = canvas.create_text(0.5 * size_of_field, 2.5 * size_of_field, text = "7", font = 30)
    _6 = canvas.create_text(0.5 * size_of_field, 3.5 * size_of_field, text = "6", font = 30)
    _5 = canvas.create_text(0.5 * size_of_field, 4.5 * size_of_field, text = "5", font = 30)
    _4 = canvas.create_text(0.5 * size_of_field, 5.5 * size_of_field, text = "4", font = 30)
    _3 = canvas.create_text(0.5 * size_of_field, 6.5 * size_of_field, text = "3", font = 30)
    _2 = canvas.create_text(0.5 * size_of_field, 7.5 * size_of_field, text = "2", font = 30)
    _1 = canvas.create_text(0.5 * size_of_field, 8.5 * size_of_field, text = "1", font = 30)

    A = canvas.create_text(1.5 * size_of_field, 0.5 * size_of_field, text = "A", font = 30)
    B = canvas.create_text(2.5 * size_of_field, 0.5 * size_of_field, text = "B", font = 30)
    C = canvas.create_text(3.5 * size_of_field, 0.5 * size_of_field, text = "C", font = 30)
    D = canvas.create_text(4.5 * size_of_field, 0.5 * size_of_field, text = "D", font = 30)
    E = canvas.create_text(5.5 * size_of_field, 0.5 * size_of_field, text = "E", font = 30)
    F = canvas.create_text(6.5 * size_of_field, 0.5 * size_of_field, text = "F", font = 30)
    G = canvas.create_text(7.5 * size_of_field, 0.5 * size_of_field, text = "G", font = 30)
    H = canvas.create_text(8.5 * size_of_field, 0.5 * size_of_field, text = "H", font = 30)

class White_Man:
    _id = []        #Canvas ID of man
    field = []      #Canvas ID of actual field 
    color = "white"
class Black_Man:
    _id = []        #Canvas ID of man
    field = []      #Canvas ID of actual field
    color = "red"

# DON'T you look at this pathetic shit
A1, B1, C1, D1, E1, F1, G1, H1, A2, B2, C2, D2, E2, F2, G2, H2, A3, B3, C3, D3, E3, F3, G3, H3, A4, B4, C4, D4, E4, F4, G4, H4, A5, B5, C5, D5, E5, F5, G5, H5, A6, B6, C6, D6, E6, F6, G6, H6, A7, B7, C7, D7, E7, F7, G7, H7, A8, B8, C8, D8, E8, F8, G8, H8 = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63
fields = [A1, B1, C1, D1, E1, F1, G1, H1, A2, B2, C2, D2, E2, F2, G2, H2, A3, B3, C3, D3, E3, F3, G3, H3, A4, B4, C4, D4, E4, F4, G4, H4, A5, B5, C5, D5, E5, F5, G5, H5, A6, B6, C6, D6, E6, F6, G6, H6, A7, B7, C7, D7, E7, F7, G7, H7, A8, B8, C8, D8, E8, F8, G8, H8]
field_dict = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7", "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8"]
# You may look at the other pathetic shit

def fields_render():        #Field IDs  17 - 80
    #LINE 1
    fields[A1] = canvas.create_rectangle(1 * size_of_field, 8 * size_of_field, 2 * size_of_field, 9 * size_of_field, fill = "black")
    fields[B1] = canvas.create_rectangle(2 * size_of_field, 8 * size_of_field, 3 * size_of_field, 9 * size_of_field, fill = "white")
    fields[C1] = canvas.create_rectangle(3 * size_of_field, 8 * size_of_field, 4 * size_of_field, 9 * size_of_field, fill = "black")
    fields[D1] = canvas.create_rectangle(4 * size_of_field, 8 * size_of_field, 5 * size_of_field, 9 * size_of_field, fill = "white")
    fields[E1] = canvas.create_rectangle(5 * size_of_field, 8 * size_of_field, 6 * size_of_field, 9 * size_of_field, fill = "black")
    fields[F1] = canvas.create_rectangle(6 * size_of_field, 8 * size_of_field, 7 * size_of_field, 9 * size_of_field, fill = "white")
    fields[G1] = canvas.create_rectangle(7 * size_of_field, 8 * size_of_field, 8 * size_of_field, 9 * size_of_field, fill = "black")
    fields[H1] = canvas.create_rectangle(8 * size_of_field, 8 * size_of_field, 9 * size_of_field, 9 * size_of_field, fill = "white")
    #LINE 2
    fields[A2] = canvas.create_rectangle(1 * size_of_field, 7 * size_of_field, 2 * size_of_field, 8 * size_of_field, fill = "white")
    fields[B2] = canvas.create_rectangle(2 * size_of_field, 7 * size_of_field, 3 * size_of_field, 8 * size_of_field, fill = "black")
    fields[C2] = canvas.create_rectangle(3 * size_of_field, 7 * size_of_field, 4 * size_of_field, 8 * size_of_field, fill = "white")
    fields[D2] = canvas.create_rectangle(4 * size_of_field, 7 * size_of_field, 5 * size_of_field, 8 * size_of_field, fill = "black")
    fields[E2] = canvas.create_rectangle(5 * size_of_field, 7 * size_of_field, 6 * size_of_field, 8 * size_of_field, fill = "white")
    fields[F2] = canvas.create_rectangle(6 * size_of_field, 7 * size_of_field, 7 * size_of_field, 8 * size_of_field, fill = "black")
    fields[G2] = canvas.create_rectangle(7 * size_of_field, 7 * size_of_field, 8 * size_of_field, 8 * size_of_field, fill = "white")
    fields[H2] = canvas.create_rectangle(8 * size_of_field, 7 * size_of_field, 9 * size_of_field, 8 * size_of_field, fill = "black")
    #LINE 3
    fields[A3] = canvas.create_rectangle(1 * size_of_field, 6 * size_of_field, 2 * size_of_field, 7 * size_of_field, fill = "black")
    fields[B3] = canvas.create_rectangle(2 * size_of_field, 6 * size_of_field, 3 * size_of_field, 7 * size_of_field, fill = "white")
    fields[C3] = canvas.create_rectangle(3 * size_of_field, 6 * size_of_field, 4 * size_of_field, 7 * size_of_field, fill = "black")
    fields[D3] = canvas.create_rectangle(4 * size_of_field, 6 * size_of_field, 5 * size_of_field, 7 * size_of_field, fill = "white")
    fields[E3] = canvas.create_rectangle(5 * size_of_field, 6 * size_of_field, 6 * size_of_field, 7 * size_of_field, fill = "black")
    fields[F3] = canvas.create_rectangle(6 * size_of_field, 6 * size_of_field, 7 * size_of_field, 7 * size_of_field, fill = "white")
    fields[G3] = canvas.create_rectangle(7 * size_of_field, 6 * size_of_field, 8 * size_of_field, 7 * size_of_field, fill = "black")
    fields[H3] = canvas.create_rectangle(8 * size_of_field, 6 * size_of_field, 9 * size_of_field, 7 * size_of_field, fill = "white")
    #LINE 4
    fields[A4] = canvas.create_rectangle(1 * size_of_field, 5 * size_of_field, 2 * size_of_field, 6 * size_of_field, fill = "white")
    fields[B4] = canvas.create_rectangle(2 * size_of_field, 5 * size_of_field, 3 * size_of_field, 6 * size_of_field, fill = "black")
    fields[C4] = canvas.create_rectangle(3 * size_of_field, 5 * size_of_field, 4 * size_of_field, 6 * size_of_field, fill = "white")
    fields[D4] = canvas.create_rectangle(4 * size_of_field, 5 * size_of_field, 5 * size_of_field, 6 * size_of_field, fill = "black")
    fields[E4] = canvas.create_rectangle(5 * size_of_field, 5 * size_of_field, 6 * size_of_field, 6 * size_of_field, fill = "white")
    fields[F4] = canvas.create_rectangle(6 * size_of_field, 5 * size_of_field, 7 * size_of_field, 6 * size_of_field, fill = "black")
    fields[G4] = canvas.create_rectangle(7 * size_of_field, 5 * size_of_field, 8 * size_of_field, 6 * size_of_field, fill = "white")
    fields[H4] = canvas.create_rectangle(8 * size_of_field, 5 * size_of_field, 9 * size_of_field, 6 * size_of_field, fill = "black")
    #LINE 5
    fields[A5] = canvas.create_rectangle(1 * size_of_field, 4 * size_of_field, 2 * size_of_field, 5 * size_of_field, fill = "black")
    fields[B5] = canvas.create_rectangle(2 * size_of_field, 4 * size_of_field, 3 * size_of_field, 5 * size_of_field, fill = "white")
    fields[C5] = canvas.create_rectangle(3 * size_of_field, 4 * size_of_field, 4 * size_of_field, 5 * size_of_field, fill = "black")
    fields[D5] = canvas.create_rectangle(4 * size_of_field, 4 * size_of_field, 5 * size_of_field, 5 * size_of_field, fill = "white")
    fields[E5] = canvas.create_rectangle(5 * size_of_field, 4 * size_of_field, 6 * size_of_field, 5 * size_of_field, fill = "black")
    fields[F5] = canvas.create_rectangle(6 * size_of_field, 4 * size_of_field, 7 * size_of_field, 5 * size_of_field, fill = "white")
    fields[G5] = canvas.create_rectangle(7 * size_of_field, 4 * size_of_field, 8 * size_of_field, 5 * size_of_field, fill = "black")
    fields[H5] = canvas.create_rectangle(8 * size_of_field, 4 * size_of_field, 9 * size_of_field, 5 * size_of_field, fill = "white")
    #LINE 6
    fields[A6] = canvas.create_rectangle(1 * size_of_field, 3 * size_of_field, 2 * size_of_field, 4 * size_of_field, fill = "white")
    fields[B6] = canvas.create_rectangle(2 * size_of_field, 3 * size_of_field, 3 * size_of_field, 4 * size_of_field, fill = "black")
    fields[C6] = canvas.create_rectangle(3 * size_of_field, 3 * size_of_field, 4 * size_of_field, 4 * size_of_field, fill = "white")
    fields[D6] = canvas.create_rectangle(4 * size_of_field, 3 * size_of_field, 5 * size_of_field, 4 * size_of_field, fill = "black")
    fields[E6] = canvas.create_rectangle(5 * size_of_field, 3 * size_of_field, 6 * size_of_field, 4 * size_of_field, fill = "white")
    fields[F6] = canvas.create_rectangle(6 * size_of_field, 3 * size_of_field, 7 * size_of_field, 4 * size_of_field, fill = "black")
    fields[G6] = canvas.create_rectangle(7 * size_of_field, 3 * size_of_field, 8 * size_of_field, 4 * size_of_field, fill = "white")
    fields[H6] = canvas.create_rectangle(8 * size_of_field, 3 * size_of_field, 9 * size_of_field, 4 * size_of_field, fill = "black")
    #LINE 7
    fields[A7] = canvas.create_rectangle(1 * size_of_field, 2 * size_of_field , 2 * size_of_field, 3 * size_of_field, fill = "black")
    fields[B7] = canvas.create_rectangle(2 * size_of_field, 2 * size_of_field , 3 * size_of_field, 3 * size_of_field, fill = "white")
    fields[C7] = canvas.create_rectangle(3 * size_of_field, 2 * size_of_field , 4 * size_of_field, 3 * size_of_field, fill = "black")
    fields[D7] = canvas.create_rectangle(4 * size_of_field, 2 * size_of_field , 5 * size_of_field, 3 * size_of_field, fill = "white")
    fields[E7] = canvas.create_rectangle(5 * size_of_field, 2 * size_of_field , 6 * size_of_field, 3 * size_of_field, fill = "black")
    fields[F7] = canvas.create_rectangle(6 * size_of_field, 2 * size_of_field , 7 * size_of_field, 3 * size_of_field, fill = "white")
    fields[G7] = canvas.create_rectangle(7 * size_of_field, 2 * size_of_field , 8 * size_of_field, 3 * size_of_field, fill = "black")
    fields[H7] = canvas.create_rectangle(8 * size_of_field, 2 * size_of_field , 9 * size_of_field, 3 * size_of_field, fill = "white")
    #LINE 8
    fields[A8] = canvas.create_rectangle(1 * size_of_field, size_of_field , 2 * size_of_field, 2 * size_of_field , fill = "white")
    fields[B8] = canvas.create_rectangle(2 * size_of_field, size_of_field , 3 * size_of_field, 2 * size_of_field , fill = "black")
    fields[C8] = canvas.create_rectangle(3 * size_of_field, size_of_field , 4 * size_of_field, 2 * size_of_field , fill = "white")
    fields[D8] = canvas.create_rectangle(4 * size_of_field, size_of_field , 5 * size_of_field, 2 * size_of_field , fill = "black")
    fields[E8] = canvas.create_rectangle(5 * size_of_field, size_of_field , 6 * size_of_field, 2 * size_of_field , fill = "white")
    fields[F8] = canvas.create_rectangle(6 * size_of_field, size_of_field , 7 * size_of_field, 2 * size_of_field , fill = "black")
    fields[G8] = canvas.create_rectangle(7 * size_of_field, size_of_field , 8 * size_of_field, 2 * size_of_field , fill = "white")
    fields[H8] = canvas.create_rectangle(8 * size_of_field, size_of_field , 9 * size_of_field, 2 * size_of_field , fill = "black")

def white_man_spawn():      #White IDs  81 - 95  odd         Text IDs  82 - 96  even
    global white_counter
    white_counter = 0
    start_position_white = [fields[A1], fields[B2], fields[C1], fields[D2], fields[E1], fields[F2], fields[G1], fields[H2]]
    for position in start_position_white:
        x1 = canvas.coords(position)[0]
        y1 = canvas.coords(position)[1]
        x2 = canvas.coords(position)[2]
        y2 = canvas.coords(position)[3]

        White_Man._id.extend([canvas.create_oval(x1, y1, x2, y2, fill = White_Man.color)])
        White_Man.field.extend([position])

        canvas.create_text((x1+x2)/2, (y1+y2)/2, text = "ID = " + str(White_Man._id[white_counter]))
        white_counter = white_counter + 1

    print("White_Man ID =", White_Man._id)
    print("White_Man Field =", White_Man.field)
    print("white_counter =", white_counter, "\n")
    return white_counter
def black_man_spawn():      #Black IDs  97 - 111 odd         Text IDs  98 - 112 even
    global black_counter
    black_counter = 0
    start_position_black = [fields[A7], fields[B8], fields[C7], fields[D8], fields[E7], fields[F8], fields[G7], fields[H8]]
    for position in start_position_black:
        x1 = canvas.coords(position)[0]
        y1 = canvas.coords(position)[1]
        x2 = canvas.coords(position)[2]
        y2 = canvas.coords(position)[3]

        Black_Man._id.extend([canvas.create_oval(x1, y1, x2, y2, fill = Black_Man.color)])
        Black_Man.field.extend([position])

        canvas.create_text((x1+x2)/2, (y1+y2)/2, text = "ID = " + str(Black_Man._id[black_counter]))
        black_counter = black_counter + 1

    print("Black_Man ID =", Black_Man._id)
    print("Black_Man Field =", Black_Man.field)
    print("black_counter =", black_counter, "\n")
    return black_counter


def find_black_fields():
    global black_fields
    black_fields = []
    for field in fields:    #Find and add black fields to array
        #field ids are from 17 to 80, so start_id compensates this 
        start_id = 17
        if field < 8 + start_id and field % 2 != 0:
            black_fields.append(field)
        elif field < 16 + start_id and field >= 8 + start_id and field % 2 == 0:
            black_fields.append(field)
        elif field < 24 + start_id and field >= 16 + start_id and field % 2 != 0:
            black_fields.append(field)
        elif field < 32 + start_id and field >= 24 + start_id and field % 2 == 0:
            black_fields.append(field)
        elif field < 40 + start_id and field >= 32 + start_id and field % 2 != 0:
            black_fields.append(field)
        elif field < 48 + start_id and field >= 40 + start_id and field % 2 == 0:
            black_fields.append(field)
        elif field < 56 + start_id and field >= 48 + start_id and field % 2 != 0:
            black_fields.append(field)
        elif field < 64 + start_id and field >= 56 + start_id and field % 2 == 0:
            black_fields.append(field)
    #print(black_fields[10], fields[20])
    return black_fields

def game():
    while white_counter != 0 and black_counter != 0:
        def move_white_man():
            def check_input():
                valid_turn = False
                global chosen_white_man
                global target_white_field
                global empty_fields

                empty_fields = black_fields   # Choose valid fields from black_fields
                for field in White_Man.field:
                    if field in empty_fields:
                        empty_fields.remove(field)
                for field in Black_Man.field:
                    if field in empty_fields:
                        empty_fields.remove(field)

                print("\n___WHITE PLAYER'S TURN___\n")
                while valid_turn == False:
                    # Coords input
                    print("Which man you wanna move?")
                    chosen_white_man = input()
                    print("\nWhere do you wanna move it?")
                    target_white_field = input()
                    chosen_white_man, target_white_field = chosen_white_man.upper(), target_white_field.upper()
                    if chosen_white_man in field_dict and target_white_field in field_dict:
                        chosen_white_man, target_white_field = field_dict.index(chosen_white_man)+17, field_dict.index(target_white_field)+17
                        if chosen_white_man in White_Man.field and (target_white_field == chosen_white_man+7 or target_white_field == chosen_white_man+9) and target_white_field in empty_fields:
                            valid_turn = True  
                            return chosen_white_man, target_white_field
                        else:
                            print("!!!INVALID INPUT!!!")
                    else:
                        print("!!!INVALID INPUT!!!")
            check_input()

            canvas.delete(White_Man._id[White_Man.field.index(chosen_white_man)])
            del White_Man._id[White_Man.field.index(chosen_white_man)]
            del White_Man.field[White_Man.field.index(chosen_white_man)]
            x1 = canvas.coords(target_white_field)[0]
            y1 = canvas.coords(target_white_field)[1]
            x2 = canvas.coords(target_white_field)[2]
            y2 = canvas.coords(target_white_field)[3]

            White_Man._id.extend([canvas.create_oval(x1, y1, x2, y2, fill = White_Man.color)])
            White_Man.field.extend([target_white_field])
            canvas.create_text((x1+x2)/2, (y1+y2)/2, text = "ID = " + str(White_Man._id[white_counter-1]))
            print("White_Man ID =", White_Man._id)
            print("White_Man Field =", White_Man.field)
            print("white_counter =", white_counter, "\n")
        move_white_man()
        def move_black_man():
            def check_input():
                valid_turn = False
                global chosen_black_man
                global target_black_field
                global empty_fields

                empty_fields = black_fields   # Choose valid fields from black_fields
                for field in Black_Man.field:
                    if field in empty_fields:
                        empty_fields.remove(field)
                for field in Black_Man.field:
                    if field in empty_fields:
                        empty_fields.remove(field)

                print("\n___BLACK PLAYER'S TURN___\n")
                while valid_turn == False:
                    # Coords input
                    print("Which man you wanna move?")
                    chosen_black_man = input()
                    print("\nWhere do you wanna move it?")
                    target_black_field = input()
                    chosen_black_man, target_black_field = chosen_black_man.upper(), target_black_field.upper()
                    if chosen_black_man in field_dict and target_black_field in field_dict:
                        chosen_black_man, target_black_field = field_dict.index(chosen_black_man)+17, field_dict.index(target_black_field)+17
                        if chosen_black_man in Black_Man.field and (target_black_field == chosen_black_man-7 or target_black_field == chosen_black_man-9) and target_black_field in empty_fields:
                            valid_turn = True  
                            return chosen_black_man, target_black_field
                        else:
                            print("!!!INVALID INPUT!!!")
                    else:
                        print("!!!INVALID INPUT!!!")
            check_input()

            canvas.delete(Black_Man._id[Black_Man.field.index(chosen_black_man)])
            del Black_Man._id[Black_Man.field.index(chosen_black_man)]
            del Black_Man.field[Black_Man.field.index(chosen_black_man)]
            x1 = canvas.coords(target_black_field)[0]
            y1 = canvas.coords(target_black_field)[1]
            x2 = canvas.coords(target_black_field)[2]
            y2 = canvas.coords(target_black_field)[3]

            Black_Man._id.extend([canvas.create_oval(x1, y1, x2, y2, fill = Black_Man.color)])
            Black_Man.field.extend([target_black_field])
            canvas.create_text((x1+x2)/2, (y1+y2)/2, text = "ID = " + str(Black_Man._id[black_counter-1]))
            print("Black_Man ID =", Black_Man._id)
            print("Black_Man Field =", Black_Man.field)
            print("black_counter =", black_counter, "\n")
        move_black_man()

    if white_counter == 0:
        print(white_counter)
        canvas.create_rectangle(size_of_field, size_of_field, 9 * size_of_field, 9 * size_of_field, fill = "yellow")
        canvas.create_text(5 * size_of_field, 5 * size_of_field, text = "Black Wins!", font = 100 )
    elif black_counter == 0:
        canvas.create_rectangle(size_of_field, size_of_field, 9 * size_of_field, 9 * size_of_field, fill = "yellow")
        canvas.create_text(5 * size_of_field, 5 * size_of_field, text = "White Wins!", font = 100 )

fields_render()
white_man_spawn()
black_man_spawn()
find_black_fields()
game()
root.mainloop()