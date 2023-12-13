import pandas as pd

df = pd.read_csv('dataset.csv')
distinct_src_ips = df['Sub_Cat'].unique()
print(distinct_src_ips)
'''
╰─ python3 examine.py                                                                                                             ─╯
['Mirai-Ackflooding' 'DoS-Synflooding' 'Scan Port OS'
 'Mirai-Hostbruteforceg' 'Mirai-UDP Flooding' 'Mirai-HTTP Flooding'
 'Normal' 'Scan Hostport' 'MITM ARP Spoofing']
'''