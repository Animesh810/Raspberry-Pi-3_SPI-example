import time
import spidev  #download this library # already downloaded in this machine
import json

CHANNEL_NUM = 16

bus = 1
device = 0 #this is the chip select pin

spi = spidev.SpiDev()
spi.open(bus, device)

#spi.max_speed_hz = 3900000  #working speed 3.9Mhz, 5.4Mhz
spi.max_speed_hz = 5400000


spi.mode = 0

time.sleep(0.005)

byte_to_send = 0xAA

dummy_send = [0x00]

start = time.time_ns()

for i in range(1,10):
    dummy_send.append(dummy_send[0] +0x00)

dump = spi.readbytes(5*CHANNEL_NUM) # just to clear the system
time.sleep(1)

for i in range(1,10000):
    to_send = []
    to_send.append(byte_to_send)
    #print("sending: ")
    #print(to_send)
    
    #spi.xfer(dummy_send)
    spi.xfer(to_send)
    #writebytes(to_send.tolist())
    #time.sleep(0.0001)
    received_bytes = spi.readbytes(CHANNEL_NUM)# use dummy variables and xfer instead of received bytes
    #spi.xfer(dump)
    #file.write(time.time())
    #file.write(',')
    
    for ch in range (1,CHANNEL_NUM):
        file_name = "testSPI[{}]"
        deli = ','
        with open(file_name.format(ch),'a') as f:
            #f.write(json.dumps(time.gmtime()))
            f.write(json.dumps(received_bytes[ch-1]))
            f.write(',')
            
    #while(received_bytes == 0): 
    print("receiving: ")
    print(received_bytes)
    #byte_to_send = byte_to_send + 0x01
    #if(byte_to_send >=0xFF):
    #   byte_to_send = 0x00
    #to_send.append(i)
    #to_send[0] = to_send[0] + 0x01
    time.sleep(0.001)
    
end = time.time_ns()

#print('time taken is:{}'.format(end) )
