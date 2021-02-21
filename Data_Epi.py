import json

# JSON数据解析
with open('EpiData.json','r',encoding = 'utf-8') as f:
    data = json.load(f)
    f.close();
# 构造echarts数据
oall = ''

for d in data:
    o1 = '{ name: \'' + d['国家'] + '\', value: ['
    o2 = '{ name: \'' + '感染人数'+ '\' , value:' + str(d['感染人数']) + '},'
    o3 = '{ name: \'' + '治愈人数'+ '\' , value:' + str(d['治愈人数']) + '},'
    o4 = '{ name: \'' + '死亡人数'+ '\' , value:' + str(d['死亡人数']) + '}]},'
    oall = oall+o1+o2+o3+o4



with open('Data_Epi.json', 'w', encoding = 'utf-8') as f:
    f.write(json.dumps(oall, ensure_ascii=False))
    f.close()
