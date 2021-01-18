from Modules.Board import *
from Modules.Man import *

def white_man_spawn():      #White IDs  81 - 95  odd         Text IDs  82 - 96  even
    White_Man.counter = 0
    start_position_white = [fields[A1], fields[B2], fields[C1], fields[D2], fields[E1], fields[F2], fields[G1], fields[H2]]
    for position in start_position_white:
        x1 = canvas.coords(position)[0]
        y1 = canvas.coords(position)[1]
        x2 = canvas.coords(position)[2]
        y2 = canvas.coords(position)[3]

        White_Man._id.extend([canvas.create_oval(x1, y1, x2, y2, fill = White_Man.color)])
        White_Man.field.extend([position])

        White_Man.counter = White_Man.counter + 1
        White_Man.lady.extend([False])

    print("White_Man ID =", White_Man._id)
    print("White_Man Field =", White_Man.field)
    print("White_Man.counter =", White_Man.counter, "\n")
def black_man_spawn():      #Black IDs  97 - 111 odd         Text IDs  98 - 112 even
    Black_Man.counter = 0
    start_position_black = [fields[A7], fields[B8], fields[C7], fields[D8], fields[E7], fields[F8], fields[G7], fields[H8]]
    for position in start_position_black:
        x1 = canvas.coords(position)[0]
        y1 = canvas.coords(position)[1]
        x2 = canvas.coords(position)[2]
        y2 = canvas.coords(position)[3]

        Black_Man._id.extend([canvas.create_oval(x1, y1, x2, y2, fill = Black_Man.color)])
        Black_Man.field.extend([position])

        Black_Man.counter = Black_Man.counter + 1
        Black_Man.lady.extend([False])

    print("Black_Man ID =", Black_Man._id)
    print("Black_Man Field =", Black_Man.field)
    print("Black_Man.counter =", Black_Man.counter, "\n")

def find_black_fields():    #Func just to identify playable fields
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
    #print(black_fields, len(black_fields))
    return black_fields

def game():                 #You may guess, what this does
    while White_Man.counter != 0 and Black_Man.counter != 0:
        def move_white_man():
            def check_input():
                valid_turn = False
                global chosen_white_man
                global target_white_field
                global empty_fields

                empty_fields = []
                empty_fields.extend(black_fields)           # Choose valid fields from black_fields
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
                        chosen_white_man, target_white_field = field_dict.index(chosen_white_man)+17, field_dict.index(target_white_field)+17           #Field IDs starts at canvas ID 17
                        #! Man or Lady movement difference
                        if White_Man.lady[White_Man.field.index(chosen_white_man)] == True:
                            #TODO Fix the Lady movement
                            if chosen_white_man in White_Man.field and (target_white_field == [chosen_white_man+7*n for n in range(-7, 8)] or target_white_field == [chosen_white_man+9*n for n in range(-7, 8)] or (target_white_field == [chosen_white_man+7+7*n for n in range(-7, 8)] and [chosen_white_man+7*n for n in range(-7, 8)] in Black_Man.field) or (target_white_field == [chosen_white_man+9+9*n for n in range(-7, 8)] and [chosen_white_man+9*n for n in range(-7, 8)] in Black_Man.field)) and target_white_field in empty_fields:
                                valid_turn = True  
                                return chosen_white_man, target_white_field
                            else:
                                print("!!!INVALID INPUT!!!")
                        else:
                            if chosen_white_man in White_Man.field and (target_white_field == chosen_white_man+7 or target_white_field == chosen_white_man+9 or (target_white_field == chosen_white_man+14 and chosen_white_man+7 in Black_Man.field) or (target_white_field == chosen_white_man+18 and chosen_white_man+9 in Black_Man.field)) and target_white_field in empty_fields:
                                valid_turn = True  
                                return chosen_white_man, target_white_field
                            else:
                                print("!!!INVALID INPUT!!!")
                    else:
                        print("!!!INVALID INPUT!!!")
            check_input()

            #! REMOVE BLACK MAN BY WHITE MAN
            if (target_white_field == chosen_white_man+14 and chosen_white_man+7 in Black_Man.field):
                Black_Man.counter = Black_Man.counter - 1
                canvas.delete(Black_Man._id[Black_Man.field.index(chosen_white_man+7)])
                del Black_Man._id[Black_Man.field.index(chosen_white_man+7)]
                del Black_Man.field[Black_Man.field.index(chosen_white_man+7)]

            elif (target_white_field == chosen_white_man+18 and chosen_white_man+9 in Black_Man.field):
                Black_Man.counter = Black_Man.counter - 1
                canvas.delete(Black_Man._id[Black_Man.field.index(chosen_white_man+9)])
                del Black_Man._id[Black_Man.field.index(chosen_white_man+9)]
                del Black_Man.field[Black_Man.field.index(chosen_white_man+9)]

            x1 = canvas.coords(target_white_field)[0]
            y1 = canvas.coords(target_white_field)[1]
            x2 = canvas.coords(target_white_field)[2]
            y2 = canvas.coords(target_white_field)[3]

            #!  Transformation to White Lady
            if target_white_field in range(73, 80):         # Canvas ID of A8 = 73, H8 = 80
                del White_Man.lady[White_Man.field.index(chosen_white_man)]
                White_Man.lady.extend([True])

            White_Man._id.extend([canvas.create_oval(x1, y1, x2, y2, fill = White_Man.color)])
            White_Man.field.extend([target_white_field])

            if White_Man.lady[White_Man.field.index(chosen_white_man)] == True:
                canvas.create_text((x1+x2)/2, (y1+y2)/2, text = "Lady", font="Times 20 italic bold")

            canvas.delete(White_Man._id[White_Man.field.index(chosen_white_man)])
            del White_Man._id[White_Man.field.index(chosen_white_man)]
            del White_Man.field[White_Man.field.index(chosen_white_man)]

            print("White_Man ID =", White_Man._id)
            print("White_Man Field =", White_Man.field)
            print("White_Man.counter =", White_Man.counter)
            print("White_Man.lady =", White_Man.lady)
        move_white_man()
            
        if White_Man.counter != 0 and Black_Man.counter != 0:
            def move_black_man():
                def check_input():
                    valid_turn = False
                    global chosen_black_man
                    global target_black_field
                    global empty_fields

                    empty_fields = []
                    empty_fields.extend(black_fields)
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
                            #! Man or Lady movement difference
                            if Black_Man.lady[Black_Man.field.index(chosen_black_man)] == True:
                                if chosen_black_man in Black_Man.field and (target_black_field == [chosen_black_man+7*n for n in range(-7, 7)] or target_black_field == [chosen_black_man+9*n for n in range(-7, 7)] or (target_black_field == [chosen_black_man+7+7*n for n in range(-7, 7)] and [chosen_black_man+7*n for n in range(-7, 7)] in White_Man.field) or (target_black_field == [chosen_black_man+9+9*n for n in range(-7, 7)] and [chosen_black_man+9*n for n in range(-7, 7)] in White_Man.field)) and target_black_field in empty_fields:
                                    valid_turn = True  
                                    return chosen_black_man, target_black_field
                                else:
                                    print("!!!INVALID INPUT!!!")
                            else:
                                if chosen_black_man in Black_Man.field and (target_black_field == chosen_black_man-7 or target_black_field == chosen_black_man-9 or (target_black_field == chosen_black_man-14 and chosen_black_man-7 in White_Man.field) or (target_black_field == chosen_black_man-18 and chosen_black_man-9 in White_Man.field)) and target_black_field in empty_fields:
                                    valid_turn = True
                                    return chosen_black_man, target_black_field
                                else:
                                    print("!!!INVALID INPUT!!!")
                        else:
                            print("!!!INVALID INPUT!!!")
                check_input()

                #! REMOVE WHITE MAN BY BLACK MAN
                if (target_black_field == chosen_black_man-14 and chosen_black_man-7 in White_Man.field):
                    White_Man.counter = White_Man.counter - 1
                    canvas.delete(White_Man._id[White_Man.field.index(chosen_black_man-7)])
                    del White_Man._id[White_Man.field.index(chosen_black_man-7)]
                    del White_Man.field[White_Man.field.index(chosen_black_man-7)]
                elif (target_black_field == chosen_black_man-18 and chosen_black_man-9 in White_Man.field):
                    White_Man.counter = White_Man.counter - 1
                    canvas.delete(White_Man._id[White_Man.field.index(chosen_black_man-9)])
                    del White_Man._id[White_Man.field.index(chosen_black_man-9)]
                    del White_Man.field[White_Man.field.index(chosen_black_man-9)]

                x1 = canvas.coords(target_black_field)[0]
                y1 = canvas.coords(target_black_field)[1]
                x2 = canvas.coords(target_black_field)[2]
                y2 = canvas.coords(target_black_field)[3]

                #! Transformation to Black Lady
                if target_black_field in range(17, 24):         # Canvas ID of A1 = 17, H1 = 24
                    del Black_Man.lady[Black_Man.field.index(chosen_black_man)]
                    Black_Man.lady.extend([True])

                Black_Man._id.extend([canvas.create_oval(x1, y1, x2, y2, fill = Black_Man.color)])
                Black_Man.field.extend([target_black_field])

                if Black_Man.lady[Black_Man.field.index(chosen_black_man)] == True:
                    canvas.create_text((x1+x2)/2, (y1+y2)/2, text = "Lady", font="Times 20 italic bold")

                canvas.delete(Black_Man._id[Black_Man.field.index(chosen_black_man)])
                del Black_Man._id[Black_Man.field.index(chosen_black_man)]
                del Black_Man.field[Black_Man.field.index(chosen_black_man)]

                print("Black_Man ID =", Black_Man._id)
                print("Black_Man Field =", Black_Man.field)
                print("Black_Man.counter =", Black_Man.counter)
                print("Black_Man.lady =", Black_Man.lady)
            move_black_man()

    if White_Man.counter == 0:
        canvas.create_rectangle(size_of_field, size_of_field, 9 * size_of_field, 9 * size_of_field, fill = "yellow", font="Times 20 italic bold")
        canvas.create_text(5 * size_of_field, 5 * size_of_field, text = "Black Wins!", font = 100 )
    elif Black_Man.counter == 0:
        canvas.create_rectangle(size_of_field, size_of_field, 9 * size_of_field, 9 * size_of_field, fill = "yellow", font="Times 20 italic bold")
        canvas.create_text(5 * size_of_field, 5 * size_of_field, text = "White Wins!", font = 100 )

fields_render()
white_man_spawn()
black_man_spawn()
find_black_fields()
game()
root.mainloop()