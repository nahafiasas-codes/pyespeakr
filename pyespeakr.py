import subprocess

def run(code,data,speed):
    if speed < 0:
        speed = 175
    subprocess.run(["espeak", "-v", code, "-s", str(speed), data])

def open_file(code,cd_file,speed):
    if speed < 0:
        speed = 175
    with open(cd_file,"r") as f:
        data_code = f.read()
        subprocess.run(["espeak", "-v", code, "-s", str(speed), data_code])

__VERSION__ = "0.3.2"
