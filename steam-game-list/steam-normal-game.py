# -*- coding:utf-8 -*-
import urllib.request
import re
page = 1
num = 0
bb = 0
file_object = open('~/steam_game.txt', 'w')

while(page<=780):
    print(type(page))
    url = "http://store.steampowered.com/search/?sort_by=Price_DESC&category1=998&page="+str(page)
    print(url)
    response = urllib.request.urlopen(url)
    print(1)
    response_str = response.read()
    print(2)
    response_str=response_str.decode('utf-8')
    print(3)
    pattern = re.compile('(<a){1}(.*?)(store.steampowered.com){1}(.*?)(search_price){1}(.*?)(</a>){1}', re.S)
    print(4)
    a = re.findall(pattern, response_str)
    print(5)
    for a_one in a :
        num += 1
        if(num >= bb):
            a_one_str = "".join(a_one)
    #         pattern_one = re.compile('(.*?)(<span class="title">){1}(.*?)(</span>){1}(.*?)'+
    #             '(col search_released responsive_secondrow">){1}(.*?)(</div>){1}(.*?)(data-store-tooltip="){1}(.*?)(">){1}(.*?)'+
    #             '(col search_price  responsive_secondrow">){1}(.*?)(</div>)' , re.S)
            pattern_one = re.compile('(.*?)(<span class="title">){1}(.*?)(</span>){1}(.*?)'+
                '(col search_released responsive_secondrow">){1}(.*?)(</div>){1}(.*?)(col search_reviewscore responsive_secondrow">){1}(.*?)(</div>){1}(.*?)'+
                '(col search_price  responsive_secondrow">){1}(.*?)(</div>)' , re.S)
            one = re.findall(pattern_one, a_one_str)
#             print(one[0])
            for b in one:
    #             print("xxx name:"+b[2].replace("\n","").replace("\t","")+"\n")
    #             print("xxx date:"+b[6].replace("\n","").replace("\t","")+"\n")
    #             print("xxx des:"+b[10].replace("\n","").replace("\t","")+"\n")
    #             print("xxx price:"+b[14].replace("\t","").replace("\n","")+"\n")
    #             print("\n")
                name = b[2].replace("\n","").replace("\t","")
                date = b[6].replace("\n","").replace("\t","")
                if(b[10].replace("\n","").replace("\t","").find("data-store-tooltip") != -1):
                    pattern_two = re.compile('(.*?)(data-store-tooltip="){1}(.*?)(">)(.*)' , re.S)
                    des_str = re.findall(pattern_two, b[10].replace("\n","").replace("\t",""))
                    des = des_str[0][2].replace("\n","").replace("\t","")
                    pattern_three = re.compile('(.*?)(of\sthe\s){1}(.*?)(\suser)(.*)' , re.S)
    #                 print(des)
                    des_str2 = re.findall(pattern_three, des)
    #                 print(des_str2)
                    des = des_str2[0][2]


                else:
                    des = "unkonwn"
                price = b[14].replace("\t","").replace("\n","")
                price_origin = price
                pattern_price = re.compile('[1-9]\d*' , re.S)
                price_str = re.findall(pattern_price,price)
    #             print(price_str)
                if(len(price_str)>=1):
                    price = price_str[0]
                else:
                    price = "unknown"
                pattern_price_free = re.compile('Free' , re.S)
                price_str_free = re.findall(pattern_price_free,price_origin)
#                 print(price_origin)
#                 print(price_str_free)
                if(len(price_str_free)>0):
                    price = "0"
                
    #             print("xxx name:"+name)
    #             print("xxx date:"+date)
    #             print("xxx des:"+des)
    #             print("xxx price:"+price)
                write_line = name+"\t"+des.replace(",","")+"\t"+price.replace(",","")+"\t"
                print(write_line)
    #             print("\n")
    #             print("\n")
    #             print("\n")
                file_object.write(write_line+'\n')
            
#             file_object.flush
    page += 1
    print(page)
    print(num)
# file_object.write("end"+'\n')
file_object.close

    
    
    
    
