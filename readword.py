

#TODO: filter A space in them
#TODO: filter A digit in them
#TODO: use on for statement/in

file=open('words.txt','r')
f=file.readlines()

new_list=[]
for line in f:
    x="-"
    if x in line: 
        continue

    if line[-1]=='\n':
        new_list.append(line[:-1])
       
    else: 
        new_list.append(line)

        

   
        
        
#for word in new_list:
    #for letter in word:
       # if letter=="-":
           # for i in range(len(new_list)):
             #   if word==new_list[i]:
               #     print(word)


