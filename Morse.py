from pydub import AudioSegment
from pydub.generators import Sine
from io import BytesIO

def morse_generator(input, tempo):

    MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', 
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
    '7': '--...', '8': '---..', '9': '----.'
    }

    ##audio lengths
    sixteenth_note = 15000 / tempo
    eigth_note = sixteenth_note * 2
    quarter_note = eigth_note * 2
    #short
    dot_sound = Sine(700).to_audio_segment(duration=sixteenth_note).apply_gain(-3) 
    #long  
    dash_sound = Sine(700).to_audio_segment(duration=eigth_note).apply_gain(-3)  
    #between beeps
    intra_symbol_gap = AudioSegment.silent(duration=sixteenth_note)
    #between letters
    inter_letter_gap = AudioSegment.silent(duration=eigth_note)
    #between words
    inter_word_gap = AudioSegment.silent(duration=quarter_note)

    def text_to_morse_audio(text):
        text = text.upper()
        result = AudioSegment.silent(duration=0)
        for i in range(4):
            result += Sine(500).to_audio_segment(duration=sixteenth_note).apply_gain(-3)
            result += AudioSegment.silent(duration=sixteenth_note * 3)
        for word in text.split():
            for letter in word:
                if letter in MORSE_CODE_DICT:
                    code = MORSE_CODE_DICT[letter]
                    for symbol in code:
                        if symbol == '.':
                            result += dot_sound
                        elif symbol == '-':
                            result += dash_sound
                        result += intra_symbol_gap
                    result += inter_letter_gap
            result += inter_word_gap

        return result
    
    def get_audio_bytes(audio_seg):
        buf = BytesIO()
        audio_seg.export(buf, format="wav")
        return buf.getvalue()
    
    audio = text_to_morse_audio(input)
    audio_byte = get_audio_bytes(audio)

    return audio_byte

