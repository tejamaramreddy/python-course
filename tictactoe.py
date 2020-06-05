import numpy as np
box = [0,1,2,3,4,5,6,7,8]
for times in range(9):
    option = input("Enter your option X or O : ")
    position = int(input("Enter the postion which you have to place : "))
    if(option.upper() == 'X' or option.upper() == 'O') and position >= 0 and position <= 8:
        if box[position] != 'X' and box[position] != 'O':
            box[position] = option.upper()
            print(np.reshape(box,(3,3)))
        else:
            print("Postion is already filled please select your option again and fill......!")
        if box[0] == 'X' and box[1] == 'X' and box[2] == 'X':
            print("X wins")
            break
        elif box[3] == 'X' and box[4] == 'X' and box[5] == 'X':
            print("X wins")
            break
        elif box[6] == 'X' and box[7] == 'X' and box[8] == 'X':
            print("X wins")
            break
        elif box[0] == 'X' and box[3] == 'X' and box[6] == 'X':
            print("X wins")
            break 
        elif box[1] == 'X' and box[4] == 'X' and box[7] == 'X':
            print("X wins")
            break
        elif box[2] == 'X' and box[5] == 'X' and box[8] == 'X':
            print("X wins")
            break
        elif box[0] == 'X' and box[4] == 'X' and box[8] == 'X':
            print("X wins")
        elif box[2] == 'X' and box[4] == 'X' and box[6] == 'X':
            print("X wins")
            break
        elif box[0] == 'O' and box[1] == 'O' and box[2] == 'O':
            print("O wins")
            break
        elif box[3] == 'O' and box[4] == 'O' and box[5] == 'O':
            print("O wins")
            break
        elif box[6] == 'O' and box[7] == 'O' and box[8] == 'O':
            print("O wins")
            break
        elif box[0] == 'O' and box[3] == 'O' and box[6] == 'O':
            print("O wins")
            break
        elif box[1] == 'O' and box[4] == 'O' and box[7] == 'O':
            print("O wins")
            break
        elif box[2] == 'O' and box[5] == 'O' and box[8] == 'O':
            print("O wins")
            break
        elif box[0] == 'O' and box[4] == 'O' and box[8] == 'O':
            print("O wins")
            break
        elif box[2] == 'O' and box[4] == 'O' and box[6] == 'O':
            print("O wins")
            break
            
    else:
        print("please enter X or O")
