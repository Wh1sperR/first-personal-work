#!/usr/bin/env python
# coding: utf-8

# In[27]:


import json
from collections import OrderedDict


# In[85]:


with open('global_epidemic_statistics.json', 'r', encoding = 'utf-8') as f:
    data = json.load(f, object_pairs_hook = OrderedDict)
    epi_whole = data['data']
    f.close()


# In[86]:


##全球
print('全球：')
print('感染人数：{}, 治愈人数：{}, 死亡人数: {}'.format(epi_whole['confirmedCount'],epi_whole['curedCount'],epi_whole['deadCount']))
print('更新时间: {}'.format(epi_whole['updateTime']))
print(epi_whole['sourceDesc'])
epi_whole = epi_whole['continent']


# In[87]:


epi_Asia = epi_whole[0]
epi_Eur = epi_whole[1]
epi_NorAm = epi_whole[2]
epi_SouAm = epi_whole[3]
epi_Africa = epi_whole[4]
epi_Oceania = epi_whole[5]
epi_Other = epi_whole[6]
print()


# In[88]:


##亚洲 epi_Asia
print('地区：{}， 感染人数：{}, 治愈人数：{}, 死亡人数: {}'.format(epi_Asia['continentName'],epi_Asia['confirmedCount'],epi_Asia['curedCount'],epi_Asia['deadCount']))
epi_Asia = epi_Asia['country']
print()
for i in range(len(epi_Asia)):
    print('国家：{}, 感染人数：{}, 治愈人数：{}, 死亡人数: {}'.format(epi_Asia[i]['provinceName'],epi_Asia[i]['confirmedCount'],epi_Asia[i]['curedCount'],epi_Asia[i]['deadCount']))


# In[89]:


##欧洲 epi_Eur
print()
print('地区：{}， 感染人数：{}, 治愈人数：{}, 死亡人数: {}'.format(epi_Eur['continentName'],epi_Eur['confirmedCount'],epi_Eur['curedCount'],epi_Eur['deadCount']))
epi_Eur = epi_Eur['country']
print()
for i in range(len(epi_Eur)):
    print('国家：{}, 感染人数：{}, 治愈人数：{}, 死亡人数: {}'.format(epi_Eur[i]['provinceName'],epi_Eur[i]['confirmedCount'],epi_Eur[i]['curedCount'],epi_Eur[i]['deadCount']))


# In[90]:


##北美洲 epi_NorAm
print()
print('地区：{}， 感染人数：{}, 治愈人数：{}, 死亡人数: {}'.format(epi_NorAm['continentName'],epi_NorAm['confirmedCount'],epi_NorAm['curedCount'],epi_NorAm['deadCount']))
epi_NorAm = epi_NorAm['country']
print()
for i in range(len(epi_NorAm)):
    print('国家：{}, 感染人数：{}, 治愈人数：{}, 死亡人数: {}'.format(epi_NorAm[i]['provinceName'],epi_NorAm[i]['confirmedCount'],epi_NorAm[i]['curedCount'],epi_NorAm[i]['deadCount']))


# In[91]:


##南美洲 epi_SouAm
print()
print('地区：{}， 感染人数：{}, 治愈人数：{}, 死亡人数: {}'.format(epi_SouAm['continentName'],epi_SouAm['confirmedCount'],epi_SouAm['curedCount'],epi_SouAm['deadCount']))
epi_SouAm = epi_SouAm['country']
print()
for i in range(len(epi_SouAm)):
    print('国家：{}, 感染人数：{}, 治愈人数：{}, 死亡人数: {}'.format(epi_SouAm[i]['provinceName'],epi_SouAm[i]['confirmedCount'],epi_SouAm[i]['curedCount'],epi_SouAm[i]['deadCount']))


# In[92]:


##非洲 epi_Africa
print()
print('地区：{}， 感染人数：{}, 治愈人数：{}, 死亡人数: {}'.format(epi_Africa['continentName'],epi_Africa['confirmedCount'],epi_Africa['curedCount'],epi_Africa['deadCount']))
epi_Africa = epi_Africa['country']
print()
for i in range(len(epi_Africa)):
    print('国家：{}, 感染人数：{}, 治愈人数：{}, 死亡人数: {}'.format(epi_Africa[i]['provinceName'],epi_Africa[i]['confirmedCount'],epi_Africa[i]['curedCount'],epi_Africa[i]['deadCount']))


# In[93]:


##大洋洲 epi_Oceania
print()
print('地区：{}， 感染人数：{}, 治愈人数：{}, 死亡人数: {}'.format(epi_Oceania['continentName'],epi_Oceania['confirmedCount'],epi_Oceania['curedCount'],epi_Oceania['deadCount']))
epi_Oceania = epi_Oceania['country']
print()
for i in range(len(epi_Oceania)):
    print('国家：{}, 感染人数：{}, 治愈人数：{}, 死亡人数: {}'.format(epi_Oceania[i]['provinceName'],epi_Oceania[i]['confirmedCount'],epi_Oceania[i]['curedCount'],epi_Oceania[i]['deadCount']))


# In[94]:


##其他 epi_Other
print()
print('地区：{}， 感染人数：{}, 治愈人数：{}, 死亡人数: {}'.format(epi_Other['continentName'],epi_Other['confirmedCount'],epi_Other['curedCount'],epi_Other['deadCount']))
epi_Other = epi_Other['country']
print()
for i in range(len(epi_Other)):
    print('国家：{}, 感染人数：{}, 治愈人数：{}, 死亡人数: {}'.format(epi_Other[i]['provinceName'],epi_Other[i]['confirmedCount'],epi_Other[i]['curedCount'],epi_Other[i]['deadCount']))


# In[ ]:




