# from midiutil import MIDIFile

# degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
# track    = 0
# channel  = 0
# time     = 0    # In beats
# duration = 1    # In beats
# tempo    = 140   # In BPM
# volume   = 100  # 0-127, as per the MIDI standard

# MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
#                       # automatically)
# MyMIDI.addTempo(track, time, tempo)

# for i, pitch in enumerate(degrees):
#     MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

# with open("major-scale.mid", "wb") as output_file:
#     MyMIDI.writeFile(output_file)

import random
from midiutil import MIDIFile
import os
import apt
cache = apt.Cache()

wildmidi = False
if cache['wildmidi'].is_installed:
    wildmidi = True

Notes = {
    'c':0,
    'c#':1,
    'd':2,
    'd#':3,
    'e':4,
    'f':5,
    'f#':6,
    'g':7,
    'g#':8,
    'a':9,
    'a#':10,
    'b':11
}
Notes_O = ['c','c#','d','d#','e','f','f#','g','g#','a','a#','b']
# Midi_Note_Number = int(Note_String[-1:])*12+Notes[Note_String[:-1]]

def midi_note_number(note):
    return int(note[-1:])*12+Notes[note[:-1]]

class Clip_T:
    def __init__(self, midi_notes, durations, accent_map=[]):
        self.midi_notes = midi_notes
        self.durations = durations
        self.accent_map = []
        if accent_map:
            for instruction in accent_map:
                if instruction is "x":
                    self.accent_map.append(127)
                elif instruction is "-":
                    self.accent_map.append(70)
        else:
            for i in range(len(midi_notes)):
                self.accent_map.append(127)
    def __repr__(self):
        return "midi_notes = {}\ndurations = {}\naccent_map = {}".format(self.midi_notes, self.durations, self.accent_map)
    def __add__(self, other):
        return Clip_T(self.midi_notes + other.midi_notes, self.durations + other.durations, self.accent_map + other.accent_map)

        
def scale(note, scale_type, octave=5):
    pattern = ''
    num = Notes[note]
    scale_notes = [note+str(octave)]
    if scale_type is "major":
        pattern = "wwhwwwh"
    elif scale_type is "minor":
        pattern = "whwwhww"
    for instruction in pattern:
        if instruction is "w":
            num += 2
        if instruction is "h":
            num += 1
        if num > 11:
            num -= 11
            octave += 1
        scale_notes.append(Notes_O[num]+str(octave))
    return scale_notes

def clip(notes, pattern="", accent_map=None, shuffle=False):
    if shuffle:
        random.shuffle(notes)
    midi_notes = []
    durations = []
    if pattern is not "":
        p = list(pattern)
        notes_index = 0
        for instruction in p:
            if instruction is "x":
                if type(notes[notes_index]) is str:
                    midi_notes.append(midi_note_number(notes[notes_index]))
                else:
                    sub_notes = []
                    for note in notes[notes_index]:
                        sub_notes.append(midi_note_number(note))
                    midi_notes.append(sub_notes)
                notes_index += 1
                durations.append(1)
            elif instruction is "-":
                midi_notes.append(-1)
            elif instruction is "_":
                midi_notes.append(-1)
                durations[len(durations)-1] += 1
            if notes_index is len(notes):
                notes_index = 0
    if accent_map is not None:
        return Clip_T(midi_notes,durations,accent_map=accent_map)
    else:
        return Clip_T(midi_notes,durations)

def midi(Clip, filename='music.mid', tempo=140):
    track = 0
    time = 0
    channel = 0
    duration = 0

    MIDI = MIDIFile(1)

    MIDI.addTempo(track, time, tempo)
    print(Clip)
    durations_index = 0
    for i, pitch in enumerate(Clip.midi_notes):
        if type(pitch) is int:
            if pitch != -1:
                MIDI.addNote(track, channel, pitch, time + i, Clip.durations[durations_index], Clip.accent_map[i])
        else:
            for pitch2 in Clip.midi_notes[i]:
                MIDI.addNote(track, channel, pitch2, time + i, Clip.durations[durations_index], Clip.accent_map[i])
        if pitch != -1: durations_index += 1

    with open(filename, "wb") as output_file:
        MIDI.writeFile(output_file)
        os.system('clear')

def play(filename='music.mid'):
    if wildmidi: os.system("wildmidi {}".format(filename))
    else: print("You must install wildmidi for this feature to work.")
