import RPi.GPIO as GPIO

import time

import socket

import sys

from gtts import gTTS

import os

import threading


class TTS(threading.Thread):

    def __init__(self):

        super().__init__()

    def run(self):

        while True:

            global class_tmp

            if class_tmp == 'with_mask':

                os.system('mpg321 with_mask.mp3')

            elif class_tmp == 'without_mask':

                os.system('mpg321 without_mask.mp3')

            elif class_tmp == 'mask_weared_incorrect':

                os.system('mpg321 mask_weared_incorrect.mp3')

            class_tmp = ''

            time.sleep(1)


global class_tmp

class_tmp = ''

thread = TTS()

thread.start()

HOST = ''  # all available interfaces

PORT = 8888

pins = (18, 19, 21)  # 빨강은 18핀, 초록은 19핀, 파랑은 21핀 지정


def led(pins, color):
    RGBs = (

        (1, 1, 1),  # 하양색

        (1, 0, 0),  # 빨강색

        (0, 1, 0),  # 초록색

        (0, 0, 1),  # 파랑색

        (0, 1, 1),  # 청록색

        (1, 0, 1),  # 보라색

        (1, 1, 0),  # 노랑색

    )

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(pins[0], GPIO.OUT)

    GPIO.setup(pins[1], GPIO.OUT)

    GPIO.setup(pins[2], GPIO.OUT)

    GPIO.output(pins[0], RGBs[color][0])

    GPIO.output(pins[1], RGBs[color][1])

    GPIO.output(pins[2], RGBs[color][2])


# 1. open Socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Socket created')

# 2. bind to a address and port

try:

    s.bind((HOST, PORT))

except socket.error as msg:

    print('Bind Failed. Error code: ' + str(msg[0]) + ' Message: ' + msg[1])

    sys.exit()

print('Socket bind complete')

# 3. Listen for incoming connections

s.listen(10)

print('Socket now listening')

# keep talking with the client

try:

    while 1:

        # 4. Accept connection

        conn, addr = s.accept()

        led(pins, 0)

        # 5. Read/Send

        data = conn.recv(1024)

        if not data:
            break

        conn.sendall(data)

        classes = data.decode().split()[2:]

        for class_ in classes:

            if "with_mask" in class_:

                led(pins, 2)

                if not os.path.exists('with_mask.mp3'):
                    tts = gTTS(text='출입하셔도 좋습니다', lang='ko')

                    tts.save('with_mask.mp3')

                class_tmp = "with_mask"

            elif "without_mask" in class_:

                led(pins, 1)

                if not os.path.exists('without_mask.mp3'):
                    tts = gTTS(text='마스크를 착용해 주세요', lang='ko')

                    tts.save('without_mask.mp3')

                class_tmp = "without_mask"

            elif "mask_weared_incorrect" in class_:

                led(pins, 6)

                if not os.path.exists('mask_weared_incorrect.mp3'):
                    tts = gTTS(text='마스크를 바르게 착용해 주세요', lang='ko')

                    tts.save('mask_weared_incorrect.mp3')

                class_tmp = "mask_weared_incorrect"





except KeyboardInterrupt:

    GPIO.cleanup(pins)

    conn.close()

    s.close()

conn.close()

s.close()