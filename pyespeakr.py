import subprocess

def if_speed(speed):
    if speed < 1:
        return 175
    return speed

# core
def run(code,data,speed):
    speed = if_speed(speed)
    subprocess.run(["espeak", "-v", code, "-s", str(speed), data])

# wrapper
def open_file(code,cd,speed):
    with open(cd,"r") as f:
        data_code = f.read()
        run(code,data_code,speed)

# core
def save_to_file(code,data,speed,name):
    speed = if_speed(speed)
    subprocess.run(["espeak", "-v", code, "-s", str(speed), data, "-w", name])

# wrapper
def file_to_voice(code,cd,speed,name):
    with open(cd,"r") as f:
        data_code = f.read()
        save_to_file(code,data_code,speed,name)

#version code
version = "0.5.9"
