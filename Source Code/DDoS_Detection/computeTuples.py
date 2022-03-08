import numpy as np
import csv


packets_csv = np.genfromtxt('data/packets.csv', delimiter=",")
dt_packets = packets_csv[:,0]
sdfp = np.std(dt_packets) 


bytes_csv = np.genfromtxt('data/bytes.csv', delimiter=",")
dt_bytes = bytes_csv[:,0]
sdfb = np.std(dt_bytes)


n_ip = np.prod(dt_bytes.shape)     
ssip = n_ip // 3               

sfe = n_ip // 3


fileone = None
filetwo = None

with open('data/ipsrc.csv', 'r') as t1, open('data/ipdst.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()


with open('data/intflow.csv','w') as f:
    for line in fileone:
        if line not in filetwo:
            f.write(line)


with open('data/intflow.csv') as f:
    reader = csv.reader(f, delimiter=",")
    dt = list(reader)
    row_count_nonint = len(dt)

rfip = abs(float(n_ip - row_count_nonint) / n_ip)

headers = ["SSIP", "SDFP", "SDFB", "SFE", "RFIP"]

features = [ssip, sdfp, sdfb, sfe, rfip]



with open('realtime.csv', 'w') as f:
    cursor = csv.writer(f, delimiter=",")
    cursor.writerow(headers)
    cursor.writerow(features)
    
    f.close()
