import json
with open('xXNCHYFvAQQ.live_chat.json', 'r', encoding='utf-8') as f:
    json_str = f.read()
    json_str = json_str.replace('}\n{','},\n{')
    json_str = json_str.replace(',,',',')

    answer = open('T1vsZETA.json','w',encoding='utf-8')
    answer.write(json_str)
    f.close()