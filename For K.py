import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("And i", 0.28),
        ("Grew up thinking I would have to fight", 0.1),
        ("All of this alone", 0.1),
        ("But now you hold me in the darkness?", 0.07),
        ("Hold me 'til it hurts less, you", 0.06),
        ("Tell me that I'm alright", 0.07),
        ("Show me where the light shines through", 0.07),
        ("Please, stay, love me through the weather", 0.079),
        ("Please, say this will be forever", 0.079),
        ("Hold me in the darkness", 0.1),
        ("Even when it's hard with you", 0.07),
        ("It's a little bit, little bit better", 0.06),
    ]
    delays = [0.2, 3.8, 10.9, 15.3, 17.9, 23.2, 23.9, 30.2, 32.4, 36.9, 38.8,42.2]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()