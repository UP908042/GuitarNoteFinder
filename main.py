
# Guitar Fret Note Finder
# Enter in a string note and fret number
# Prints out what note that fret is

# A, A#, B, C, C#, D, D#, E, F, F#, G, G#
# 12 Notes in an Octave
# Each note is put into a list in order so assigned an index value from 0-11
# you input a string note and fret number it adds string note + fret number and then % by 12 to get the new note.

def FretNoteFinder():
    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    print("Enter a String")
    string = input()
    print("Enter a Fret Number")
    fret = int(input())

    noteNum = (notes.index(string) + fret) % 12

    print(notes[noteNum])

if __name__ == '__main__':
    FretNoteFinder()