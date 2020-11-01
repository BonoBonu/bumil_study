class Stack:
    # 빈 스택을 배열로 초기화
    def __init__(self):
        self.data = [] 
        
    # 스택의 크기
    def size(self):
        return len(self.data)
    
    # 빈 스택 판단 여부
    def isEmpty(self):
        return self.size() == 0
    
    # 데이터 원소 추가
    def push(self, item):
        self.data.append(item)
        
    # 데이터 원소 삭제 (리턴)
    def pop(self):
        return self.data.pop()
    
    # 스택의 꼭대기 원소 반환
    def peek(self):
        return self.data[-1]


# 주문표를 나누어 연산자를 추가하고 피연산자와 연산자를 구분해 리스트로 만든다
def splitTokens(exprStr):
    tokens=[]
    val=""       #문자
    for c in exprStr:
        #숫자일 경우 뒤에 *붙이기
        if c in '0123456789' :
            #숫자 앞에 괄호나 문자가 있을 경우 + 붙이기
            if len(tokens)>1 and tokens[len(tokens)-1]==')':
                tokens.append('+')
            if val!='':
                tokens.append(val)
                val=''
                tokens.append('+')
            tokens.append(int(c))
            tokens.append('*')
        elif c=='(':
            if val!='':
                #문자 뒤에 괄호가 올 경우 ^붙이기
                #문자 여러개가 붙어있을경우 한개만 자르기
                if len(val)>1:
                    tokens.append(val[:-1:])
                    tokens.append('+')
                    tokens.append(val[-1::])
                    tokens.append('^')
                else:  
                    tokens.append(val)
                    tokens.append('^')
                val=''
            tokens.append(c)
        #괄호 안 문자 넣기 and 뒤에 문자나 숫자가 올 경우 + 붙이기
        elif c==')':
            if val!='':
                tokens.append(val)
                val=''
            tokens.append(c)
        else:
            if len(tokens)>1 and tokens[len(tokens)-1]==')':
                tokens.append('+')
            val+=c
            
    #뒤에 남은 문자 추가하기
    if val!='':
                tokens.append(val)  
    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*' : 3,
        '^' : 3,
        '+' : 2,
        '(' : 1
    }
    opStack = Stack()
    postfixList = []

    for token in tokenList:
        # 피연산자이면 리스트에 추가
        if type(token) is int or token not in '*^+()':
            postfixList.append(token)
        # '('이면 스택에 push
        elif token == '(':
            opStack.push(token)
            
        # ')' 이면 '('가 나올때까지 pop
        elif token == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()
        
        # 연산자이면 +-*/
        else:
            # 스택이 비어있을 경우 스택에 push
            if opStack.isEmpty():
                opStack.push(token)
                
            # 스택이 비어있지 않다면 비교
            else:
                
                # 스택에 값이 존재할 동안에 반복
                while opStack.size() > 0:
                    # 우선 순위가 스택안에 있는게 높으면 꺼낸다
                    if prec[opStack.peek()] >= prec[token]:
                        postfixList.append(opStack.pop())
                    else:
                        break
                
                opStack.push(token)
            
    # 반복문을 다 돌고 스택이 빌때까지 pop
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    
    # 리스트로 리턴한다
    return postfixList


def postfixEval(tokenList):
    valStack = Stack()
    
    for token in tokenList:
        # 피연산자를 만나면 스택에 push
        if type(token) is int or token not in '*^+()':
            valStack.push(token)
            
        # 연산자를 만나면
        elif token == '+':
            n1 = str(valStack.pop())
            n2 = str(valStack.pop())
            valStack.push(n2+n1)
        #숫자일 경우
        elif token == '*':
            n1 = valStack.pop()
            n2 = valStack.pop()
            valStack.push(n2*n1)
        #문자일 경우
        elif token == '^':
            n1 = valStack.pop()
            n2 = valStack.pop()
            n=''
            for c in n1:
                n+=n2
                n+=c
            valStack.push(n)
        
    return valStack.pop()


    
order=input()
tokens = splitTokens(order)
postfix = infixToPostfix(tokens)
val = postfixEval(postfix)

print(val)
