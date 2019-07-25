from flask import Flask
import subprocess

state = 'stop'

app = Flask(__name__)


@app.route('/<direction>')
def main(direction):
    global state

    if direction in ['forward', 'left', 'right', 'stop']:
      print(f"Processing {direction}")
      if state != direction:
        subprocess.run(["C:\Program Files\AutoHotkey\AutoHotkey.exe", f"stop.ahk"])
        state = direction
        subprocess.run(["C:\Program Files\AutoHotkey\AutoHotkey.exe", f"{direction}.ahk"])

    return  '', 204

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8098)