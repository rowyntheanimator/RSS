import chatter
import pygame

font_map = {
    "A": [
        (1, 0), (2, 0), (3, 0),
        (0, 1), (4, 1),
        (0, 2), (4, 2),
        (0, 3), (4, 3),
        (0, 4), (4, 4),
        (1, 2), (2, 2), (3, 2),
    ],
    "B": [
        (0, 0), (1, 0), (2, 0),
        (0, 1), (3, 1),
        (0, 2), (3, 2),
        (0, 3), (3, 3),
        (0, 4), (2, 4),
        (1, 2), (2, 2), (3, 2),
        (1, 4),
    ],
    "C": [
        (1, 0), (2, 0), (3, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 4), (2, 4), (3, 4),
    ],
    "H": [
        (0, 0), (4, 0),
        (0, 1), (4, 1),
        (0, 2), (4, 2),
        (0, 3), (4, 3),
        (0, 4), (4, 4),
        (1, 2), (2, 2),
        (3, 2),
    ],
    "E": [
        (0, 0), (1, 0), (2, 0),
        (0, 1),
        (0, 2), (1, 2), (2, 2),
        (0, 3),
        (0, 4), (1, 4), (2, 4),
    ],
    "L": [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4), (1, 4), (2, 4),
    ],
    "O": [
        (1, 0), (2, 0), (3, 0),
        (0, 1), (4, 1),
        (0, 2), (4, 2),
        (0, 3), (4, 3),
        (1, 4), (2, 4), (3, 4),
    ],
    "W": [ 
        (0, 0), (2, 0), (4, 0),
        (0, 1), (2, 1), (4, 1),
        (0, 2), (2, 2), (4, 2),
        (0, 3), (2, 3), (4, 3),
        (1, 4), (3, 4),
    ],
    "R": [
        (0, 0), (1, 0), (2, 0), (3, 0),
        (0, 1), (4, 1),
        (0, 2), (1, 2), (2, 2), (3, 2),
        (0, 3), (1, 3),
        (0, 4), (2, 4),
    ],
    "D": [
        (0, 0), (1, 0), (2, 0), (3, 0),
        (0, 1), (4, 1),
        (0, 2), (4, 2),
        (0, 3), (4, 3),
        (0, 0), (1, 0), (2, 4), (3, 4),
        (0, 4), (1, 4),
    ],
    "S": [
        (1, 0), (2, 0), (3, 0),
        (0, 1),
        (0, 2), (3, 2),
        (3, 3),
        (1, 4), (2, 4), (3, 4),
    ],
    "F": [
        (0, 0), (1, 0), (2, 0),
        (0, 1),
        (0, 2), (1, 2), (2, 2),
        (0, 3),
        (0, 4),
    ],
    "G": [
        (1, 0), (2, 0), (3, 0), (4, 0),
        (0, 1),
        (0, 2), (2, 2), (3, 2),
        (0, 3), (4, 3),
        (1, 4), (2, 4), (3, 4),
        (4, 4),
        (4, 2),
    ],
    "I": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (2, 1),
        (2, 2),
        (2, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
    ],
    "J": [
        (4, 0),
        (4, 1),
        (4, 2),
        (4, 3), (0, 3),
        (3, 4), (2, 4), (2, 4), (1, 4)
    ],
    "K": [
        (0, 0), (3, 0),
        (0, 1), (2, 1),
        (0, 2), (1, 2),
        (0, 3), (2, 3),
        (0, 4), (3, 4),
    ],
    "M": [
        (1, 0), (3, 0),
        (0, 1), (2, 1), (4, 1),
        (0, 2), (2, 2), (4, 2),
        (0, 3), (2, 3), (4, 3),
        (0, 4), (2, 4), (4, 4),
    ],
    "N": [
        (4, 0), (1, 1), (0, 0),
        (4, 1), (2, 2), (0, 1),
        (4, 2), (3, 3), (0, 2),
        (4, 3), (0, 3),
        (4, 4), (0, 4),
    ],
    "P": [
        (0, 0), (1, 0), (2, 0), (3, 0),
        (0, 1), (4, 1), (4, 1),
        (0, 2), (1, 2), (2, 2), (3, 2),
        (0, 3),
        (0, 4),
    ],
    "Q": [
        (1, 0), (2, 0), (3, 0),
        (0, 1), (4, 1),
        (0, 2), (4, 2),
        (0, 3), (4, 3),
        (1, 4), (2, 4), (3, 4),
        (3, 3),
        (4, 4),
        (2, 2),
    ],
    "S": [
        (1, 0), (2, 0), (3, 0), (4, 0),
        (0, 1),
        (1, 2), (2, 2), (3, 2),
        (4, 3),
        (0, 4), (1, 4), (2, 4), (3, 4),
    ],
    "T": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (2, 1),
        (2, 2),
        (2, 3),
        (2, 4),
    ],
    "U": [
        (0, 0), (4, 0),
        (0, 1), (4, 1),
        (0, 2), (4, 2),
        (0, 3), (4, 3),
        (1, 4), (2, 4), (3, 4),
    ],
    "V": [
        (0, 0), (4, 0),
        (0, 1), (4, 1),
        (0, 2), (4, 2),
        (1, 3), (3, 3),
        (2, 4),
    ],
    "W": [
        (0, 0), (2, 0), (4, 0),
        (0, 1), (2, 1), (4, 1),
        (0, 2), (2, 2), (4, 2),
        (0, 3), (2, 3), (4, 3),
        (1, 4), (3, 4),
    ],
    "X": [
        (0, 0), (4, 0),
        (1, 1), (3, 1),
        (2, 2),
        (1, 3), (3, 3),
        (0, 4), (4, 4)
    ],
    "Y": [
        (0, 0), (4, 0),
        (0, 1), (4, 1),
        (1, 2), (3, 2),
        (2, 3),
        (2, 4),
    ],
    "Z": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (3, 1),
        (2, 2),
        (1, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
    ],
    "1": [
        (0, 0), (1, 0), (2, 0),
        (2, 1),
        (2, 2),
        (2, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
    ],
    "2": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (4, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (0, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
    ],
    "3": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (4, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (4, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
    ],
    "4": [
        (0, 0), (4, 0),
        (0, 1), (4, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (4, 3),
        (4, 4),
    ],
    "5": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (0, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (4, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
    ],
    "6": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (0, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (0, 3), (4, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
    ],
    "7": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (4, 1),
        (4, 2),
        (3, 3),
        (3, 4),
    ],
    "8": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (0, 1), (4, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (0, 3), (4, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
    ],
    "9": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (0, 1), (4, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (4, 3),
        (4, 4),
    ],
    "0": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (0, 1), (4, 1),
        (0, 2), (4, 2),
        (0, 3), (4, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
    ],
    "+": [
        (2, 0),
        (2, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (2, 3),
        (2, 4),
    ],
    "-": [
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
    ],
    "=": [
        (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
        (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
    ],
    "*": [
        (2, 0),
        (2, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (2, 3),
        (2, 4),
        (1, 1),
        (0, 0),
        (4, 0),
        (3, 1),
        (4, 4),
        (0, 4),
        (3, 3),
        (1, 3),
    ],
    "d": [
        (3, 0),
        (3, 1),
        (2, 2),
        (1, 3),
        (1, 4),
    ],
    ".": [
        (0, 4),
    ],
    "?": [
        (0, 0), (1, 0), (2, 0),
        (2, 1),
        (1, 2), (2, 2),
        (1, 4)
    ],
    "!": [
        (2, 0),
        (2, 1),
        (2, 2),
        (2, 4)
    ],
    ":": [
        (2, 1),
        (2, 3),
    ],
    ";": [
        (2, 1),
        (2, 3),
        (2, 4),
    ],
    ",": [
        (2, 3),
        (1, 4),
    ],
    "l": [
        (1, 0), (2, 0),
        (1, 1),
        (1, 2), (0, 2),
        (1, 3),
        (1, 4), (2, 4),
    ],
    "r": [
        (3, 0), (2, 0),
        (3, 1),
        (3, 2), (4, 2),
        (3, 3),
        (3, 4), (2, 4),
    ],
    "[": [
        (1, 0), (2, 0),
        (1, 1),
        (1, 2),
        (1, 3),
        (1, 4), (2, 4),
    ],
    "]": [
        (3, 0), (2, 0),
        (3, 1),
        (3, 2),
        (3, 3),
        (3, 4), (2, 4),
    ],
    "q": [
        (1, 1), (3, 1),
        (1, 2), (3, 2)
    ],
    "w": [
        (2, 1),
        (2, 2),
    ],
    "g": [
        (2, 0), (3, 0), (4, 0),
        (1, 1),
        (0, 2),
        (1, 3),
        (2, 4), (3, 4), (4, 4),
    ],
    "h": [
        (0, 0), (1, 0), (2, 0),
        (3, 1),
        (4, 2),
        (3, 3),
        (0, 4), (1, 4), (2, 4),
    ],
    "j": [
        (2, 0),
        (2, 1),
        (2, 2),
        (2, 3),
        (2, 4),
    ],
    "k": [
        (1, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (3, 4),
    ],
    "s": [
        (3, 0),
        (3, 1),
        (2, 2),
        (1, 3),
        (1, 4),
    ],
    "░": [
        (0, 0), (2, 0), (4, 0),
        (0, 2), (2, 2), (4, 2),
        (0, 4), (2, 4), (4, 4),
    ],
    "▒": [
        (0, 0), (2, 0), (4, 0),
        (1, 1), (3, 1),
        (0, 2), (2, 2), (4, 2),
        (1, 3), (3, 3),
        (0, 4), (2, 4), (4, 4),
    ],
    "▓": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (1, 1), (3, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (1, 3), (3, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
    ],
    "█": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
    ],
    "─": [
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2),
    ],
    "│": [
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
    ],
    "┌": [
        (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
        (2, 2), (3, 2), (4, 2), (5, 2),
    ],
    "┐": [
        (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
        (2, 2), (1, 2), (0, 2), (-1, 2),
    ],
    "└": [
        (2, 2), (2, 1), (2, 0), (2, -1), (2, -2), (2, -3),
        (2, 2), (3, 2), (4, 2), (5, 2),
    ],
    "┘": [
        (2, 2), (2, 1), (2, 0), (2, -1), (2, -2), (2, -3),
        (2, 2), (1, 2), (0, 2), (-1, 2),
    ],
    "├": [
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
        (2, 2), (3, 2), (4, 2), (5, 2),
    ],
    "┤": [
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
        (2, 2), (1, 2), (0, 2), (-1, 2),
    ],
    "┬": [
        (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2),
    ],
    "┴": [
        (2, -2), (2, -1), (2, 0), (2, 1), (2, 2),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2),
    ],
    "┼": [
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2),
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
    ],
    " ": [],
}

def display_character(x, y, char, color, scale=2):
    """Display a character on the screen by drawing its corresponding pixels."""
    if char in font_map:
        for (dx, dy) in font_map[char]:
            for ix in range(scale):
                for iy in range(scale):
                    chatter.graphics(x + dx * scale + ix, y + dy * scale + iy, color)

def display_text(x, y, text, color, scale=2):
    """Display a string of text at the given position."""
    posE = x
    position = x
    positiony = y
    for char in text:
        if char == "/":
            positiony = positiony + (8 * scale)
            position = posE
        display_character(position, positiony, char, color, scale)
        if not char == "/":
            position += (6 * scale)

def upper(x):
    if x == "q":
        y = "Q"
    elif x == "w":
        y = "W"
    elif x == "e":
        y = "E"
    elif x == "r":
        y = "R"
    elif x == "t":
        y = "T"
    elif x == "y":
        y = "Y"
    elif x == "u":
        y = "U"
    elif x == "i":
        y = "I"
    elif x == "o":
        y = "O"
    elif x == "p":
        y = "P"
    elif x == "a":
        y = "A"
    elif x == "s":
        y = "S"
    elif x == "d":
        y = "D"
    elif x == "f":
        y = "F"
    elif x == "g":
        y = "G"
    elif x == "h":
        y = "H"
    elif x == "j":
        y = "J"
    elif x == "k":
        y = "K"
    elif x == "l":
        y = "L"
    elif x == "z":
        y = "Z"
    elif x == "x":
        y = "X"
    elif x == "c":
        y = "C"
    elif x == "v":
        y = "V"
    elif x == "b":
        y = "B"
    elif x == "n":
        y = "N"
    elif x == "m":
        y = "M"
    elif x == "space":
        y = " "
    elif x == "return":
        y = "/"
    elif x == "[+]":
        y = "+"
    elif x == "[-]":
        y = "-"
    elif x == "[*]":
        y = "*"
    elif x == "left shift":
        y = ""
        chatter.audio(800, 0.1)
    elif x == "right shift":
        y = ""
        chatter.audio(800, 0.1)
    elif x == "/":
        y = "s"
    elif x == "[/]":
        y = "s"
    elif x == "tab":
        y = "    "
    elif x == "caps lock":
        y = ""
        chatter.audio(800, 0.1)
    elif x == "numlock":
        y = ""
        chatter.audio(800, 0.1)
    elif x == "[1]":
        y = "1"
    elif x == "[2]":
        y = "2"
    elif x == "[3]":
        y = "3"
    elif x == "[4]":
        y = "4"
    elif x == "[5]":
        y = "5"
    elif x == "[6]":
        y = "6"
    elif x == "[7]":
        y = "7"
    elif x == "[8]":
        y = "8"
    elif x == "[9]":
        y = "9"
    elif x == "[0]":
        y = "0"
    elif x == "up":
        y = ""
        chatter.audio(800, 0.1)
    elif x == "down":
        y = ""
        chatter.audio(800, 0.1)
    elif x == "left":
        y = ""
        chatter.audio(800, 0.1)
    elif x == "right":
        y = ""
        chatter.audio(800, 0.1)
    else:
        y = x
    return y

text1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ/1234567890//HELLO WORLD.//1+1=2/1-1=0/1X1=1/1d1=1//1+1=2... OR IS IT 20?!?/SYMBOLS: :;,.?![]lrqwghjk/GRAPHIC: ░▒▓█/──/│/│//┌┬┐/├┼┤/└┴┘/│ │/├┼┤/│ │/"
text2 = "TYPE SOMETHING:/" # long ^^^                                                       it has not ended yet??                                                          Finally..
text3v1 = "CHOOSE./1 TECH DEMO g-/2 TEXT EDITOR/3 PAINT PROGRAM"
text3v2 = "CHOOSE./1 TECH DEMO/2 TEXT EDITOR g-/3 PAINT PROGRAM"
text3v3 = "CHOOSE./1 TECH DEMO/2 TEXT EDITOR/3 PAINT PROGRAM g-"
var = text3v1
alt_mode = "no"
ctr_mode = "no"
display_text_dis = "yes"
Rmode = False
press = None  # Ensure press is defined before entering the loop

while True:
    chatter.clear(chatter.black)
    if display_text_dis == "yes":
        display_text(0, 9, var, chatter.green, scale=3)
    chatter.display_screen()
    while True:
        chatter.clear(chatter.black)
        chatterinput = chatter.input()
        display_text(0, 9, var, chatter.green, scale=3)
        chatter.display_screen()
        if chatterinput == "down":
            if var == text3v1:
                var = text3v2
            elif var == text3v2:
                var = text3v3
            elif var == text3v3:
                var = text3v1
        elif chatterinput == "up":
            if var == text3v1:
                var = text3v3
            elif var == text3v2:
                var = text3v1
            elif var == text3v3:
                var = text3v2
        elif chatterinput == "return":
            if var == text3v1:
                press = "1"
            elif var == text3v2:
                press = "2"
            elif var == text3v3:
                press = "3"
            break
    if press == "1":
        chatter.audio(400, 0.1)
        display_text_dis = "yes"
        var = text1
    if press == "2":
        display_text_dis = "yes"
        chatter.audio(400, 0.1)
        var = text2
        while True:
            press = upper(press)
            chatter.clear(chatter.black)
            display_text(0, 9, text2, chatter.green, scale=3)
            chatter.display_screen()
            press = upper(chatter.input())
            if alt_mode == "yes":
                if press == ",":
                    ndr = "g"
                elif press == ".":
                    ndr = "h"
                elif press == "s":
                    ndr = "?"
                elif press == ";":
                    ndr = ":"
                elif press == "\'":
                    ndr = "q"
                elif press == "[":
                    ndr = "l"
                elif press == "]":
                    ndr = "r"
                elif press == "\\":
                    ndr = "j"
                elif press == "1":
                    ndr = "!"
                else:
                    ndr = press
            if alt_mode == "no":
                if press == ",":
                    ndr = ","
                elif press == ".":
                    ndr = "."
                elif press == "/":
                    ndr = "/"
                elif press == ";":
                    ndr = ";"
                elif press == "\'":
                    ndr = "w"
                elif press == "[":
                    ndr = "["
                elif press == "]":
                    ndr = "]"
                elif press == "\\":
                    ndr = "k"
                else:
                    ndr = press
            if ctr_mode == "yes":
                if press == "Q":
                    ndr = "░"
                elif press == "W":
                    ndr = "▒"
                elif press == "E":
                    ndr = "▓"
                elif press == "R":
                    ndr = "█"
                elif press == "T":
                    ndr = "─"
                elif press == "Y":
                    ndr = "│"
                elif press == "U":
                    ndr = "┌"
                elif press == "I":
                    ndr = "┐"
                elif press == "O":
                    ndr = "└"
                elif press == "P":
                    ndr = "┘"
                elif press == "A":
                    ndr = "├"
                elif press == "S":
                    ndr = "┤"
                elif press == "D":
                    ndr = "┬"
                elif press == "F":
                    ndr = "┴"
                elif press == "G":
                    ndr = "┼"
                else:
                    ndr = press
            if not press == "None" and not press == "backspace" and not press == "left alt" and not press == "right alt" and not press == "left ctrl" and not press == "right ctrl":
                text2 = str(text2 + str(ndr))
            if press == "backspace":
                if text2:
                    text2 = text2[:-1]
            if press == "left alt":
                alt_mode = "yes"
                chatter.audio(600, 0.1)
            if press == "right alt":
                alt_mode = "no"
                chatter.audio(500, 0.1)
            if press == "left ctrl":
                ctr_mode = "yes"
                chatter.audio(600, 0.1)
            if press == "right ctrl":
                ctr_mode = "no"
                chatter.audio(500, 0.1)
    if press == "3":
        chatter.audio(400, 0.1)
        R, G, B = chatter.green
        color = R, G, B
        chatter.clear(chatter.black)
        display_text_dis = "no"
        scale = 10
        back = chatter.black
        while True:
            press = chatter.input()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            xd, yd = chatter.get_mouse_position()
            mouse_state = chatter.get_mouse_state()
            left_click = mouse_state.get("left_click", False)
            right_click = mouse_state.get("right_click", False)
            scroll_up = mouse_state.get("scroll_up", False)
            scroll_down = mouse_state.get("scroll_down", False)
            if left_click:
                for dx in range(scale):
                    for dy in range(scale):
                        chatter.graphics(xd + dx, yd + dy, color)
            if right_click:
                for dx in range(scale):
                    for dy in range(scale):
                        chatter.graphics(xd + dx, yd + dy, back)
            if scroll_up:
                scale += 5
            if scroll_down:
                scale -= 5
            if press == "r":
                Rmode = False
            if press == "t":
                Rmode = True
            if Rmode:
                if press == "q" and R <= 254:
                    R += 1
                if press == "a" and R >= 1:
                    R -= 1
                if press == "w" and G <= 254:
                    G += 1
                if press == "s" and G >= 1:
                    G -= 1
                if press == "e" and B <= 254:
                    B += 1
                if press == "d" and B >= 1:
                    B -= 1
                color = (R, G, B)
            print(color)
            chatter.display_screen()


