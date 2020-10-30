cement=0 #시멘트 양

day = int(input("벽돌: "))
width=int(input("너비: "))

brick=[0]*width #벽돌쌓기 리스트

for i in range(day):
    print(str(i+1)+" 일차:",end=' ')
    wall=input().split(' ')
    
    #벽돌 input 받아서 쌓기
    pos=int(0);
    for n in wall:
        brick[pos]+=int(n)
        pos+=1;
        
    num=int(max(brick)) #젤 높은 벽돌 높이

    #한 줄씩 시멘트 넣기
    for height in range(num):      
        up=[]

        #벽돌 한줄씩 
        for n in brick:
            if n-height>0:
                up.append(int(1))
            else:
                up.append(int(0))
                
        left=int(0)#왼쪽 확인점
        right=int(width-1)#오른쪽 확인점
        
        #확인점이 만나거나 사이에 공간이 없으면 break
        while right-left!=0 and right-left!=1:
            #확인점 사이 시멘트넣는 공간있는지 확인 
            if up[left]==1 and up[right]==1:
                for n in range(left,right+1):
                    #시멘트 넣기
                    if up[n]==0:
                        brick[n]+=1
                        cement+=1
                break
            #공간이 없으면 확인점 옮기기
            elif up[left]==0:
                left+=1
            elif up[right]==0:
                right-=1
                
print(cement) #답       
