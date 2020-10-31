cement=0 #시멘트 양

day = int(input("일: "))
width=int(input("너비: "))

wall=[0]*width #벽돌쌓기 리스트

for i in range(day):
    print(str(i+1)+" 일차:",end=' ')
    brick=input().split(' ')
    for w in range(width):
        wall[w]+=int(brick[w])
    
    
    wall_list=list(set(wall))#정렬+중복 제거
    wall_list.sort(reverse=True)#벽돌 높은 순서정렬

    
    for n in wall_list:
        pos=int(0)
        #높은 벽돌 순서대로 오른쪽 왼쪽 스캔
        for j in wall:
            left=int(pos)
            right=int(pos)
            if j==n:
                if left>1:
                    for l in range(left-1,0,-1):
                        if wall[l]>=j:
                            #시멘트 채우기
                            for ce in range(l+1,left):
                                cement+=j-wall[ce]
                                wall[ce]=j
                            break
                if right<width-1:
                    for r in range(right+1,width):
                        if wall[r]>=j:
                            #시멘트 채우기
                            for ce in range(right+1,r):
                                cement+=j-wall[ce]
                                wall[ce]=j
                            break
            pos+=1
print(cement)
