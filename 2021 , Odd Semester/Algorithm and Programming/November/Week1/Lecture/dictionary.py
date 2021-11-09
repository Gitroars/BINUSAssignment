# def countWords(myStr):
#     myDict={}
#     splitWords=myStr.split()
#     for word in splitWords:
#         myDict[word]=myDict.get(word,0)+1
#     return myDict
# myStr=input(("Enter: "))
# myWordCount=countWords(myStr)
# for key in myWordCount:
#     print(myWordCount[key],key)
def from10(k,n):
  li=[]
  digit=0
  while k**digit<=n:
    digit+=1
  digit-=1

  while digit>=0:
    val=1
    while val*(k**digit)<=n:
        val+=1
    val-=1
    li.append(val)
    n=n-(val*(k**digit))
    digit-=1
  return li
print(from10(8,2345890))