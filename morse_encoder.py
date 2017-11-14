# Copyright 2017 Gerwin Sturm
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

_morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----"
}

def _encode_letter(char):
    if char in _morse.keys():
        return _morse[char]
    return " "

def _signal_from_morse(char, high=100, low=0):
    if char == ".":
        return [high, low]
    if char == "-":
        return [high, high, high, low]
    
    return [low, low]

def text_2_morse(text):
    """Convert text to a String in morse code"""
    return " ".join((_encode_letter(char) for char in text.upper()))

def text_2_signals(text, high=100, low=0):
    """Converts a text into a list of high/low morse signals"""
    morse = "    " + text_2_morse(text)
    return (_signal_from_morse(char, high, low) for char in morse)
