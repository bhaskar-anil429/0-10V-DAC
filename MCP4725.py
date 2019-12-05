import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)
# 0x60 --- i2c address
# 0x41 -- DAC cahnnel one
while True:
    for i in range(0,4095):
        data1 = (i>>4)
        data2 = (i&15)<<4
        data = [data1, data2]
        bus.write_i2c_block_data(0x60, 0x41, data)
        time.sleep(0.01)
        print "Writing on DAC %d DAC value " %i
        i = i+1
