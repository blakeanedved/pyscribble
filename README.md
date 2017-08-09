# pyscribble
A scribbletune-like library for python3

## pyscribble.clip(note_list, pattern='', accent_map=None, shuffle=False)
### note_list = ['c5','d5,'f#5','d#5']
note format: note (lowercase, no flats) + octave (0-10)
you can also use nested lists to play multiple notes at once
### pattern = "x_--x_--x_--x_--"
x = note on,
\- = note off,
_ = sustain note
### accent_map = "x---x---x---x---"
x = high accent,
\- = low accent
### shuffle = True
randomly shuffle the notes array before assembling the midi file

---

## pyscribble.scale(note, type='major', octave=5)
### note = 'c'
any note on the scale (excluding flats)
### type = 'major'
type of scale (major/minor)
### octave = 5
the octave that the scale will start in

---

## pyscribble.midi(Clip, filename='music.mid')
### Clip = pyscribble.Clip
1 or more Clips added together
### filename = "music.mid"
the filename to save the midi data to

---

## pyscribble.play(filename='music.mid')
### THE LINUX PACKAGE wildmidi IS REQUIRED FOR THIS FEATURE TO WORK
### filename = "music.mid"
the filename to load and play the midi file from