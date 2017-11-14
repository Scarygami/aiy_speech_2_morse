#!/usr/bin/env python3
# Copyright 2017 Gerwin Sturm
# Adapted from https://github.com/google/aiyprojects-raspbian/tree/voicekit/ Copyright 2017 Google Inc.
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
#


"""Converting speech via the Google CloudSpeech recognizer to morse."""

import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import itertools

from aiy_speech_2_morse_led import LED
from morse_encoder import text_2_signals, text_2_morse

_GPIO_LED = 25

def main():
    recognizer = aiy.cloudspeech.get_recognizer()

    button = aiy.voicehat.get_button()
    led = LED(_GPIO_LED)
    led.start()
    
    aiy.audio.get_recorder().start()
    text = None

    while True:
        print("Press the button and speak")
        button.wait_for_press()
        print("Listening...")
        led.set_state(LED.PULSE_QUICK)
        text = recognizer.recognize()

        if not text:
            print("Sorry, I did not hear you.")
            let.set_state(LED.OFF)
        else:
            if "goodbye" in text:
                break

            print("You said: ", text)
            print("Morse: ", text_2_morse(text))
            iterator = itertools.chain.from_iterable(text_2_signals(text))
            led.set_iterator(iterator, 0.20)
            
    led.stop()

if __name__ == '__main__':
    main()
