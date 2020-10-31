player = int(input("참여 수: "))

fast=int(input("빠른사람 수: "))

print("빠른 사람:",end=' ')
faster=input().split(' ')

game=int(input("게임 수: "))

print("이동:",end=' ')
mv=input().split(' ')

pos=int(0) #술래 위
p=int(65) #술래
score=[0]*player #술래 횟수
score[0]+=1

#앉은 사람이름 아스키코드 리스트
play=[]
for i in range(66,65+player):
    play.append(int(i))
    
#게임 횟수
for go in range(game):
    #수건 놓는 위치
    touch=int(mv[go])
    if touch>0:
        touch=(touch+pos)%(player-1)
    else:
        touch=abs(touch)%(player-1)
        if touch>pos:
            touch=(player-1)-touch
        else:
            touch=pos-touch
    pos=touch

    #술래 찾기
    if chr(play[touch]) in faster:
        score[p-65]+=1
        
    else:
        t=p
        p=play[touch]
        score[play[touch]-65]+=1
        play[touch]=t
        
for ans in range(player):
    print(chr(ans+65)+" "+str(score[ans]))        
