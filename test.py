import json

file = open("Noto_ANN_miss.json", "r", encoding="utf-8")
data = file.read()
lines = str(data).split("\n")
# print(lines)

f = open('Noto_ANN.txt','w', encoding='UTF-8')

#i = 0
for line in lines:
    #for文のどこでエラーが起きているか確認用
    #print(line)
    #print(i)
    #i += 1
    if line == "":
        continue
    lJson = json.loads(line)
    jAction = lJson["replayChatItemAction"]["actions"][0]
    if "addChatItemAction" in jAction:
        jItem = jAction["addChatItemAction"]["item"]
        if "liveChatTextMessageRenderer" in jItem:
            try:

                commentContent = jItem["liveChatTextMessageRenderer"]["message"]["runs"][0]["text"]
                f.writelines(commentContent)
            except:
                commentContent = jItem["liveChatTextMessageRenderer"]["message"]["runs"][0]["emoji"]
                #commentContent = jItem["liveChatTextMessageRenderer"]["message"]["runs"]["emoji"][0]["emojiId"]
                f.writelines(commentContent)
            print(str(commentContent))

f.close()
