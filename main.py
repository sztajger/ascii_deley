#ascii_deley 
#Send an ASCII-Modbus frame with a user-defined inter-character deley.
#
#requirements: pip install pyserial

import serial
import time

# -------- port settings -------------
PORT = "COM5"                   # change to your serial port you use
BAUDRATE = 9600                 # must mach tha X110 ASCII settings
DELEY_S = 0.10                 # gap between characters (>1s -> should be rejected)
FRAME_TX = ":03010102F9\r\n"    # frame we test in full ASCII include CRLF
# ------------------------------------

def main() -> None:
    with serial.Serial(
        port=PORT,
        baudrate=BAUDRATE,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=3
    ) as ser:


        print(f"Sending fram with {DELEY_S:2f}s gap between bytes ...")
        for ch in FRAME_TX.encode("ascii"):
            ser.write(bytes([ch]))
            time.sleep(DELEY_S)
        print("Frame sent. Waiting for response ...")

        response = ser.read(64)
        if response:
            print("Device responded  ➜ ", response.decode(errors="ignore"))
        else:
            print("No response (expected if device rejects the frame)")



if __name__ == "__main__":
    main()