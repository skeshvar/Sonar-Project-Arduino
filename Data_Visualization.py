import serial as sr
import numpy as np
import matplotlib.pyplot as plt
import time
pi = np.pi
FONT = 17

def Basic():   
    FONT = 17
    x1 = np.linspace(0, 1, 100)
    x2 = np.linspace(0, 2, 100)
    x3 = np.linspace(0, 3, 100)
    x4 = np.linspace(0, 4, 100)
    
    y1 = np.sqrt(1-x1**2)
    y2 = np.sqrt(4-x2**2)
    y3 = np.sqrt(9-x3**2)
    y4 = np.sqrt(16-x4**2)
     
    plt.plot( x1, y1, 'g', linewidth=2)
    plt.plot(-x1, y1, 'g', linewidth=2)
    plt.plot( x2, y2, 'g', linewidth=2)
    plt.plot(-x2, y2, 'g', linewidth=2)
    plt.plot( x3, y3, 'g', linewidth=2)
    plt.plot(-x3, y3, 'g', linewidth=2)
    plt.plot( x4, y4, 'g', linewidth=2)
    plt.plot(-x4, y4, 'g', linewidth=2)
    plt.plot([-4, 4], [0, 0], 'g', linewidth=2)
    
    plt.plot([0, 4*np.cos(pi/6)], [0, 4*np.sin(pi/6)], 'g', linewidth=2)
    plt.plot([0, 4*np.cos(pi/3)], [0, 4*np.sin(pi/3)], 'g', linewidth=2)
    plt.plot([0, 4*np.cos(pi/2)], [0, 4*np.sin(pi/2)], 'g', linewidth=2)
    plt.plot([0, 4*np.cos(2*pi/3)], [0, 4*np.sin(2*pi/3)], 'g', linewidth=2)
    plt.plot([0, 4*np.cos(5*pi/6)], [0, 4*np.sin(5*pi/6)], 'g', linewidth=2)
    
    plt.text(-4.2, -0.15, '40cm', color= 'g', fontsize=FONT)
    plt.text(-3.2, -0.15, '30cm', color= 'g', fontsize=FONT)
    plt.text(-2.2, -0.15, '20cm', color= 'g', fontsize=FONT)
    plt.text(-1.2, -0.15, '10cm', color= 'g', fontsize=FONT)
    
    plt.text(4.04*np.cos(pi/6),  4.04*np.sin(pi/6), r'$30^{0}$', color= 'g', fontsize=FONT)
    plt.text(4.05*np.cos(pi/3),  4.05*np.sin(pi/3), r'$60^{0}$', color= 'g', fontsize=FONT)
    plt.text(4.1*np.cos(pi/2),  4.1*np.sin(pi/2), r'$90^{0}$', color= 'g', fontsize=FONT)
    plt.text(4.2*np.cos(2*pi/3),  4.2*np.sin(2*pi/3), r'$120^{0}$', color= 'g', fontsize=FONT)
    plt.text(4.3*np.cos(5*pi/6),  4.2*np.sin(5*pi/6), r'$150^{0}$', color= 'g', fontsize=FONT)
    plt.axis('off')
    return()


duration = 30
ArduinoSerialData = sr.Serial('com3', 2e6, timeout=2)

currentTime = time.time()


plt.style.use('dark_background')
plt.figure('Sonar', figsize=(15, 10))
Basic() 
plt.ylim(0, 4.5)
plt.xlim(-4, 4)

while (currentTime+duration > time.time() ):
    if (ArduinoSerialData.inWaiting())>0:
        MyData = ((ArduinoSerialData.readline()).decode()).split(',')
        try:
            A, B = float(MyData[0]), float(MyData[1])
            
            if (B<40):
                ANG = plt.text(1.5, -0.3, str(A)+ r' $^{o}$', fontsize=FONT, color="r")
                DIS = plt.text(2.5, -0.3, str(B)+ " cm",  fontsize=FONT, color="r")
                Plot1 = plt.plot([0, 4*np.cos(A*pi/180) ], [0, 4*np.sin(A*pi/180)], 
                                 color='g', linewidth=30, alpha= 0.4)
                Plot2 = plt.scatter(B/10*np.cos(A*pi/180), B/10*np.sin(A*pi/180), 
                                    marker='o', color='r', zorder=5, s=130)
                plt.pause(0.001)
                ANG.remove()
                DIS.remove()
                (Plot1.pop(0)).remove()
                Plot2.remove()
            else:
                ANG = plt.text(1.5, -0.3, str(A)+ r' $^{o}$', fontsize=15, color="g")
                Plot1 = plt.plot([0, 4*np.cos(A*pi/180) ], [0, 4*np.sin(A*pi/180)], color='g',
                                 linewidth=30, alpha= 0.4)
                plt.pause(0.001)
                ANG.remove()
                (Plot1.pop(0)).remove()

        except(IndexError) or (ValueError):
            pass 
    else:
        continue 

ArduinoSerialData.close()




