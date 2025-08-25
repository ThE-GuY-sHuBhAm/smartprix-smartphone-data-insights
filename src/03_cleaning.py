#!/usr/bin/env python
# coding: utf-8

# In[954]:


import numpy as np
import pandas as pd


# In[955]:


df = pd.read_excel('phones_data.xlsx')


# In[956]:


df.sample(5)


# ## Data Assessing
# 
# ### Quality Issues
# 
# 1. **model** - some brands are written diiferently like OPPO in model column `consistency`
# 2. **price** - has unneccesary '₹' `validity`
# 3. **price** - has ',' between numbers `validity`
# 4. **ratings** - missing values `completeness`
# 5. **processor** - has some incorrect values for some samsung phones(row # -446,474,535,720,825,866,883,1004,395,463,486,511,524,556,561,649,653,704,705,754,808,823,839,844,894,909,1003,814,929,934,611,812) `validity`
# 6. **memory** - incorrect values in rows (284,395,446,535,618,649,808,812,814,823,825,839,844,845,866,883,929,1004) `validity`
# 7. **battery** - incorrect values in rows(446,472,474,488,524,535,556,561,649,704,720,808,812,814,823,825,839,844,866,883,929,1000,1004) `validity`
# 8. **display** - sometimes frequency is not available `completeness`
# 9. **display** - incorrect values in rows(446,474,488,524,535,556,561,599,611,649,679,704,720,808,812,814,823,825,839,844,866,883,929,1000,1004) `validity`
# 10. certain phones are foldable and the info is scattered `validity`
# 11. **camera** - words like Dual, Triple and Quad are used to represent number of cameras and front and rear cameras are separated by '&'
# 12. **camera** - problem with rows (188,264,283,377,407,417,429,443,446,449,472,474,487,488,505,524,535,555,556,561,571,611,625,649,650,679,684,685,704,720,756,757,758,808,812,814,823,825,832,834,839,844,856,866,913,916,924,928,929,968,1004) `validity`
# 13. **card** - sometimes contains info about os and camera `validity`
# 14. **os** - sometimes contains info about bluetooth and fm radio `validity`
# 15. **os** - issue with rows (324,378) `validity`
# 16. **os** - sometimes contains os version name like lollipop `consistency`
# 17. missing values in camera, card and os `completeness`
# 18. datatype  of price and rating is incorrect `validity`
# 
# 
# 
# ### Tidiness Issues
# 
# 1. **sim** - can be split into 3 cols has_5g, has_NFC, has_IR_Blaster
# 2. **ram** - can be split into 2 cols RAM and ROM
# 3. **processor** - can be split into processor name, cores and cpu speed.
# 4. **battery** - can be split into battery capacity, fast_charging_available
# 5. **display** - can be split into size, resolution_width, resolution_height and frequency
# 6. **camera** - can be split into front and rear camera
# 7. **card** - can be split into supported, extended_upto

# In[957]:


df.info()


# In[958]:


df.describe()


# In[959]:


df.isnull().sum()


# In[960]:


df1=df.copy()


# In[961]:


df1['price']=df1['price'].str.replace('₹',"").str.replace(',','').astype(int)


# In[962]:


df.head()


# In[963]:


df1=df1.reset_index()


# In[964]:


df1['index']=df1['index']+2


# In[965]:


df1.head()


# In[966]:


processor_rows = set((446,474,535,720,825,866,883,1004,395,463,486,511,524,556,561,649,653,704,705,754,808,823,839,844,894,909,1003,814,929,934,611,812))
ram_rows = set((284,395,446,535,618,649,808,812,814,823,825,839,844,845,866,883,929,1004))
#284,618,845, has only rom
#909,1003, has only ram
battery_rows = set((446,472,474,488,524,535,556,561,649,704,720,808,812,814,823,825,839,844,866,883,929,1000,1004))
display_rows = set((446,474,488,524,535,556,561,599,611,649,679,704,720,808,812,814,823,825,839,844,866,883,929,1000,1004))
camera_rows = set((188,264,283,377,407,417,429,443,446,449,472,474,487,488,505,524,535,555,556,561,571,611,625,649,650,679,684,685,704,720,756,757,758,808,812,814,823,825,832,834,839,844,856,866,913,916,924,928,929,968,1004))           


# In[967]:


df1[df1['index'].isin(processor_rows| ram_rows| battery_rows |display_rows|display_rows|camera_rows)]


# In[968]:


df1[df1['index'].isin(processor_rows & ram_rows & battery_rows & display_rows & display_rows & camera_rows)]


# In[969]:


df1[df1['index'].isin(processor_rows & ram_rows & battery_rows & display_rows & display_rows & camera_rows)]['price'].mean()


# In[970]:


df1=df1[df1['price']>=3400]


# In[971]:


df1[df1['index'].isin(processor_rows & ram_rows & battery_rows & display_rows & display_rows & camera_rows)]


# In[972]:


df1[df1['index'].isin(processor_rows)]


# In[973]:


df1.drop([522,559],inplace=True)


# In[974]:


df1[df1['index'].isin(ram_rows)]


# In[975]:


df1[df1['index'].isin(battery_rows)]


# In[976]:


temp_df=df1[df1['index'].isin(battery_rows)]


# In[977]:


x = temp_df.iloc[:,7:].shift(1,axis=1).values


# In[978]:


df1.loc[temp_df.index,temp_df.columns[7:]] = x


# In[979]:


df1['index']


# In[980]:


df1[df1['index'].isin(display_rows)]


# In[981]:


display_df=df1.loc[[677]]


# In[982]:


x = display_df.iloc[:,7:].shift(1,axis=1).values
df1.loc[display_df.index,temp_df.columns[7:]] = x


# In[983]:


df1[df1['index'].isin(camera_rows)]


# In[984]:


camera_df=df1[df1['index'].isin(camera_rows)]


# In[985]:


camera_df=camera_df[~camera_df['camera'].str.contains("MP")]


# In[986]:


camera_df


# In[987]:


df1.loc[camera_df.index,"camera"] = camera_df['card'].values


# In[988]:


df1[df1['index'].isin(camera_rows)]


# In[989]:


df1['card'].value_counts()


# In[990]:


temp_new_df=df1[df1['card'].str.contains("MP")]


# In[991]:


df1.loc[temp_new_df.index,'card'] = 'Memory Card Not Supported'


# In[992]:


temp_new_df


# In[993]:


temp_new_df


# In[994]:


temp_df = df1[df1['os'] == 'Bluetooth']
df1.loc[temp_df.index,'os'] = np.nan


# In[995]:


df1['os'].value_counts()


# In[996]:


temp_df = df1[df1['os'] == 'No FM Radio']
df1.loc[temp_df.index,'os'] = np.nan


# In[997]:


df1['os'].value_counts()


# In[998]:


df1['card'].value_counts()


# In[999]:


df1[['card','os']].sample(50)


# In[1000]:


import re
# Make sure blanks are NaN
df1[['os','card']] = df1[['os','card']].replace(r'^\s*$', np.nan, regex=True)

OS_RE   = r'(?:Android|iOS|Blackberry)'   
CARD_RE = r'Memory\s*Card'               

def keep_os(x):
    return x if isinstance(x, str) and re.search(OS_RE, x, flags=re.I) else np.nan

def keep_card(x):
    return x if isinstance(x, str) and re.search(CARD_RE, x, flags=re.I) else np.nan

# Extract candidates from both columns
os_from_os     = df1['os'].apply(keep_os)
os_from_card   = df1['card'].apply(keep_os)
card_from_card = df1['card'].apply(keep_card)
card_from_os   = df1['os'].apply(keep_card)

# Rebuild clean columns with a clear priority:
# - OS: prefer the value already in 'os'; if missing, take it from 'card'
# - Card: prefer the value already in 'card'; if missing, take it from 'os'
df1['os']   = os_from_os.combine_first(os_from_card)
df1['card'] = card_from_card.combine_first(card_from_os)

# Final safety net: purge any residual cross-contamination
df1.loc[df1['os'].str.contains(CARD_RE, case=False, na=False), 'os'] = np.nan
df1.loc[df1['card'].str.contains(OS_RE,  case=False, na=False), 'card'] = np.nan


# In[1001]:


df1['card'].value_counts()


# In[1002]:


df1['os'].value_counts()


# In[1003]:


df1[['card','os']].sample(25)


# In[1004]:


df1.shape


# In[1005]:


df1.head()


# In[1006]:


brand_names = df1['model'].str.split(" ").str.get(0)


# In[1007]:


df1.insert(1,'brand_name',brand_names)


# In[1008]:


df1


# In[1009]:


df1['brand_name']=df1['brand_name'].str.lower()


# In[1010]:


df1


# In[1011]:


has_5g=df1['sim'].str.contains("5G")
has_nfc=df1['sim'].str.contains("NFC")
has_ir_blaster=df1['sim'].str.contains("IR Blaster")


# In[1012]:


df1.insert(6,'has_5g',has_5g)
df1.insert(7,'has_nfc',has_nfc)
df1.insert(8,'has_ir_blaster',has_ir_blaster)


# In[1013]:


df1.head()


# In[1014]:


processor_name=df1['processor'].str.split(',').str.get(0)


# In[1015]:


num_cores = df1['processor'].str.split(',').str.get(1)


# In[1016]:


processor_speed = df1['processor'].str.split(',').str.get(2)


# In[1017]:


df1.insert(10,'processor_name',processor_name)
df1.insert(11,'num_cores',num_cores)
df1.insert(12,'processor_speed',processor_speed)


# In[1018]:


df1['processor_name'].value_counts().sample(50)


# In[1019]:


temp_df=df1[df1['processor_name'].str.contains("Core")][['processor_name','num_cores','processor_speed']].shift(1,axis=1)


# In[1020]:


df1.loc[temp_df.index,['processor_name','num_cores','processor_speed']] =temp_df.values


# In[1021]:


df1['processor_name'].value_counts().sample(50)


# In[1022]:


processor_brand_name = df1['processor_name'].str.split(" ").str.get(0).str.lower()


# In[1023]:


df1.insert(11, 'processor_brand',processor_brand_name)


# In[1024]:


df1['processor_brand'] = df1['processor_brand'].str.strip()


# In[1025]:


df1['processor_brand'].value_counts()


# In[1026]:


df1['num_cores']=df1['num_cores'].str.strip()


# In[1027]:


df1['num_cores'].value_counts()


# In[1028]:


df1['num_cores'] = df1['num_cores'].replace({
    'Octa Core Processor': 'Octa Core',
    'Nine-Cores': 'Nine Core',
    'Nine Cores': 'Nine Core'
})


# In[1029]:


df1['num_cores'].value_counts()


# In[1030]:


df1['processor_speed'] = df1['processor_speed'].str.strip().str.split(" ").str.get(0).str.replace("\u2009"," ").str.split(" ").str.get(0).astype(float)


# In[1031]:


df1.head()


# In[1032]:


ram_capacity = df1['ram'].str.strip().str.split(',').str.get(0).str.findall(r'\b(\d+)\b').str.get(0)


# In[1033]:


df1.insert(15,'ram_capacity',ram_capacity)


# In[1034]:


df1.head()


# In[1035]:


internal_memory = df1['ram'].str.strip().str.split(',').str.get(1).str.strip().str.findall(r'\b(\d+)\b').str.get(0)


# In[1036]:


df1.insert(16,'internal_memory',internal_memory)


# In[1037]:


df1.head()


# In[1038]:


df1['ram_capacity'].value_counts().sort_values(ascending=False)


# In[1039]:


df1['ram_capacity'] = df1['ram_capacity'].astype(float)
df1['internal_memory'] = df1['internal_memory'].astype(float)


# In[1040]:


df1[df1['ram_capacity'] > 24]


# In[1041]:


fix_idx = [282, 616, 843]

df1.loc[fix_idx, 'internal_memory'] = df1.loc[fix_idx, 'ram_capacity']
df1.loc[fix_idx, 'ram_capacity'] = 8.0


# In[1042]:


df1[df1['model'] == 'Apple iPhone 16 Plus (256GB)']


# In[1043]:


temp_df = df1[df1['internal_memory'] == 1]
df1.loc[temp_df.index,'internal_memory'] = 1024


# In[1044]:


df1['internal_memory'].value_counts()


# In[1045]:


df1[df1['internal_memory'] == 1024]


# In[1046]:


battery_capacity=df1['battery'].str.strip().str.split("with").str.get(0).str.strip().str.findall(r'\b(\d+)\b').str.get(0).astype(float)


# In[1047]:


df1.insert(18,'battery_capacity',battery_capacity)


# In[1048]:


df1.columns.tolist()


# In[1049]:


fast_charging = df1['battery'].str.strip().str.split("with").str.get(1).str.strip().str.findall(r'(\d+)').str.get(0)


# In[1050]:


df1.insert(19,'fast_charging',fast_charging)


# In[1051]:


df1['fast_charging'] = df1['fast_charging'].fillna('-1')


# In[1052]:


df1['fast_charging'] = df1['fast_charging'].astype(int)


# In[1053]:


df1.columns.tolist()


# In[1054]:


screen_size = df1['display'].str.strip().str.split(',').str.get(0).str.strip().str.split(' ').str.get(0).astype(float)


# In[1055]:


df1.insert(21,'screen_size',screen_size)


# In[1056]:


resolution = df1['display'].str.strip().str.split(',').str.get(1).str.strip().str.split('px').str.get(0)


# In[1057]:


df1.insert(22,'resolution',resolution)


# In[1058]:


refresh_rate = df1['display'].str.strip().str.split(',').str.get(2).str.findall(r'(\d+)').str.get(0).apply(lambda x: 60 if pd.isna(x) else x).astype(int)
                                                                                            


# In[1059]:


df1.insert(23,'refresh_rate',refresh_rate)


# In[1060]:


df1.head()


# In[1061]:


df1['camera'].value_counts()


# In[1062]:


def camera_extractor(text):
    if "Quad" in text:
        return 4
    elif "Triple" in text:
        return 3
    elif "Dual" in text:
        return 2
    else:
        return 1


# In[1063]:


num_rear_cameras = df1['camera'].str.split('&').str.get(0).apply(camera_extractor)


# In[1064]:


df1.insert(25,'num_rear_cameras',num_rear_cameras)


# In[1065]:


def front_camera_extractor(text):

  if 'Quad' in text:
    return '4'
  elif 'Triple' in text:
    return '3'
  elif 'Dual' in text:
    return '2'
  elif 'Missing' in text:
    return 'Missing'
  else:
    return '1'


# In[1066]:


num_front_camera = df1['camera'].str.split('&').str.get(1).str.strip().fillna('Missing').apply(front_camera_extractor)


# In[1067]:


df1.insert(26,'num_front_camera',num_front_camera)


# In[1068]:


primary_camera_rear = df1['camera'].str.split("&").str.get(0).str.split("+").str.get(0).str.strip().str.split("MP").str.get(0)


# In[1069]:


df1.insert(27,'primary_camera_rear',primary_camera_rear)


# In[1070]:


primary_camera_front = df1['camera'].str.split("&").str.get(1).str.split("+").str.get(0).str.findall(r'(\d+)').str.get(0).astype(float)


# In[1071]:


df1.insert(28,'primary_camera_front',primary_camera_front)


# In[1072]:


df1.columns.tolist()


# In[1073]:


df1['primary_camera_rear'].value_counts()


# In[1074]:


df1[df1['primary_camera_rear'] == 'Foldable Display, Dual Display']


# In[1075]:


mask_infinix = df1['model'].str.contains("Infinix Zero Flip", case=False, na=False)
mask_samsung = df1['model'].str.contains("Galaxy Z Flip 4", case=False, na=False)


# In[1076]:


df1.loc[mask_infinix, 'primary_camera_rear'] = "50"
df1.loc[mask_infinix, 'primary_camera_front'] = "50"

df1.loc[mask_samsung, 'primary_camera_rear'] = "12"
df1.loc[mask_samsung, 'primary_camera_front'] = "10"


# In[1077]:


df1.loc[mask_infinix | mask_samsung, ['model','primary_camera_rear','primary_camera_front']]


# In[1078]:


df1['primary_camera_rear'].value_counts()


# In[1079]:


df1['primary_camera_rear'] = df1['primary_camera_rear'].astype(float)


# In[1080]:


df1['os'].value_counts()


# In[1081]:


df1['os'].isna().sum()


# In[1082]:


nan_df = df1[df1['os'].isna()]
nan_df


# In[1083]:


df1.loc[nan_df.index, 'os'] = 'Android'


# In[1084]:


df1['os'].isna().sum()


# In[1085]:


def os_transform(text):
    if "Android" in text:
        return "android"
    elif "iOS" in text: 
        return "iOS"
    else:
        return "other"


# In[1086]:


df1['os'] = df1['os'].apply(os_transform)


# In[1087]:


df1.head(3)


# In[1088]:


df1.columns.tolist()


# In[1089]:


df1['fast_charging'].value_counts()


# In[1090]:


def fast_charging_or_not(num):
    if num != -1:
        return 1
    else: 
        return -1


# In[1091]:


df1['fast_charging_available']=df1['fast_charging'].apply(fast_charging_or_not)


# In[1092]:


df1.insert(19, 'fast_charging_available', df1.pop('fast_charging_available'))


# In[1093]:


df1['fast_charging_available'].value_counts()


# In[1094]:


df1['card'].value_counts()


# In[1095]:


def extended_memory_supported(text):
    if text =="Memory Card Not Supported":
        return 0
    else:
        return 1


# In[1096]:


df1['memory_card_supported']=df1['card'].apply(extended_memory_supported)


# In[1097]:


df1.insert(30, 'memory_card_supported', df1.pop('memory_card_supported'))


# In[1098]:


df1['memory_card_supported'].value_counts()


# In[1101]:


df1.count()


# In[1102]:


df['card'].str.strip().str.split(',').str.get(1).str.strip().str.split('TB').str.get(0)[3]


# In[1103]:


import re

def extract_memory_capacity(val):
    if not isinstance(val, str): 
        return np.nan

    val = val.replace("\u2009", "").replace("\u202f", "").strip()
    
    if "Not Supported" in val:
        return 0

    match = re.search(r"(\d+)\s*(GB|TB)", val, flags=re.IGNORECASE)
    if match:
        num = int(match.group(1))
        unit = match.group(2).upper()
        return num * 1024 if unit == "TB" else num

    return np.nan


# In[1104]:


df1['extended_memory'] = df1['card'].apply(extract_memory_capacity)


# In[1105]:


df1.insert(32, 'extended_memory', df1.pop('extended_memory'))


# In[1106]:


df1['extended_memory'].isna().sum()


# In[1107]:


df1['extended_memory'].value_counts()


# In[1112]:


df1.columns.tolist()


# In[1119]:


df1.drop(columns=['index','sim','processor','processor_name','ram','battery','display','camera','card'],inplace=True)


# In[1120]:


df1.info()


# In[1121]:


df1.to_excel("cleaned__smartphone_data.xlsx", index=False)


# In[ ]:




