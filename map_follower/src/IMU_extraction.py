def serconvert(ser_cmd):
    if 'I' in ser_cmd and 'U' in ser_cmd:
        s = ser_cmd.index('I')
        e = ser_cmd.index('U')
        if s > e:
            print('s > e')
            e = ser_cmd.index('U',e+1)
            car_ser = ser_cmd[s:e+1]
            ax = int(car_ser[1:6])
            ay = int(car_ser[6:11])
            print(ax,ay)
        else:
            print('s < e')
            car_ser = ser_cmd[s:e+1]
            ax = int(car_ser[1:6])
            ay = int(car_ser[6:11])
            print(ax,ay)
    else:
        print('No valid IMU reading')
        car_ser = ''
    return car_ser
	    
