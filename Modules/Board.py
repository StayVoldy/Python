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
