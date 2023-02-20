#集合運算

s1={2,3,4,5}
s2={3,4,5,6}

print(10 in s1)#判斷式，會輸出布林值
print(3 not in s1)

#交集：&是取兩個集合中相同的資料

s3=s1&s2
print(s3)

#聯集：取出兩個集合中的所有資料，但不重複

s3=s1|s2
print(s3)

#差集：從前面的集合中，去除與後面集合相同的資料

s3=s1-s2
print(s3)

#反交集：取兩個集合中，不重複的資料
s3=s1^s2
print(s3)

#set(字串)，可猜解字串成一個字母集合
s=set("Hello")
print(s)

#字典運算： key-value配對
dic={"apple": "蘋果","banana":"香蕉"}

#輸入key的值後，所提取出來的會是value的值
print(dic["apple"])

#替換掉key所對應的value
dic["apple"]="咬一口蘋果"

#判斷key是否存在字典中
print("apple" in dic)
print("tomato" not in dic)

#del 為刪除字典中的key以及所對應的value(鍵值對)
dic1={"apple": "蘋果","banana":"香蕉"}
print(dic1)
del dic["apple"]
print(dic1)

#從列表的資料中產生字典
dic2={x:x*2 for x in [1,2,3,4,5,6,7]}
print(dic2)