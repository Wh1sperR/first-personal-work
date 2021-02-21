import json

# JSON数据解析
with open('EpiData.json','r',encoding = 'utf-8') as f:
    data = json.load(f)
    f.close();
# 构造echarts数据
oall = ''

for d in data:
    o1 = '{ name: \'' + d['国家'] + '\', value:' + str(d['感染人数']) + '},'
    oall = oall+o1

with open('Data_Color.json', 'w', encoding = 'utf-8') as f:
    f.write(json.dumps(oall, ensure_ascii=False))
    f.close()
