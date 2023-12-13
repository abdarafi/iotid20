import pandas as pd
df = pd.read_csv('dataset.csv')

# I feel Sub_Cat can be dropped?
# df.drop('Sub_Cat', axis=1, inplace=True)
# Can remove the duplicate records too if necessary?
# df = df.drop_duplicates()

def split_ip(ip):
    octets = ip.split('.')
    return [int(octet) for octet in octets]

df[['Src_IP_oct1', 'Src_IP_oct2', 'Src_IP_oct3', 'Src_IP_oct4']] = df['Src_IP'].apply(lambda x: pd.Series(split_ip(x)))
df[['Dst_IP_oct1', 'Dst_IP_oct2', 'Dst_IP_oct3', 'Dst_IP_oct4']] = df['Dst_IP'].apply(lambda x: pd.Series(split_ip(x)))

df.drop(['Src_IP', 'Dst_IP'], axis=1, inplace=True)

df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['Day_of_Week'] = df['Timestamp'].dt.day_name()
df['Hour'] = df['Timestamp'].dt.hour
df['AM_PM'] = df['Timestamp'].dt.strftime('%p')

label_mapping = {'normal': 0, 'anomaly': 1}
category_mapping = {'normal': 0, 'Mirai': 1, 'DoS': 2, 'Scan': 3, 'MITM': 4}

df['Label'] = df['Label'].map(label_mapping)
df['Category'] = df['Category'].map(category_mapping)

df.to_csv('processed_dataset.csv', index=False)