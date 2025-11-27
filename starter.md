# 1번
```
def solution(number1, number2):
    answer = number1 + number2
    return answer
```

# 3번
```
def solution(number1, number2):
    answer = number1 - number2
    return answer
```

# 4번
```
def solution(number1, number2):
    answer = number1 * number2
    return answer
```

# 5번
```
def solution(number1, number2):
    answer = number1 / number2 * 100
    return int(answer)
```

# 6번
```
def solution(number1, number2):
    answer = number1 // number2
    return answer
```

# 7번
```
def solution(number1, number2):
    answer = number1 % number2
    return answer
```

# 8번
```
def solution(number, exponent):
    answer = number ** exponent
    return answer
```

# 9번
```
def solution(number):
    answer = number **0.5
    return int(answer)
```

# 10번
```
def solution(number1, number2):
    if number1 > number2:
        answer = number1
    else:
        answer = number2
    return answer
```

---

# 11번
```
def solution(number):
    if number % 2 == 0 :
        answer = '짝수'
    else:
        answer = '홀수'
    return answer
```

# 12번
```
def solution(number):
    if number > 0:
        answer = "POSITIVE"
    elif number == 0 :
        answer = "ZERO"
    else:
        answer = "NEGATIVE"
    return answer
```

# 13번
```
def solution(number, start, end):
    if start <= number <= end:
        answer = "YES"
    else:
        answer = "NO"
    return answer
```

# 14번
```
def solution(score):
    if score >= 90 :
        answer = "A"
    elif score >= 80:
        answer = "B"
    elif score >= 70:
        answer = "C"
    elif score >= 60:
        answer = "D"
    else:
        answer = "F"
    return answer
```

# 15번
```
def solution(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        answer = "YES"
    else:
        answer = "NO"
    return answer
```

# 16번
```
def solution(weight, height):
    bmi = weight / (height*height)
    if bmi >= 25 :
        answer = "비만"
    elif  bmi >= 23 :
        answer = "과체중"
    elif bmi >= 18.5:
        answer = "정상"
    else:
        answer = "저체중"
    return answer
```

# 17번
```
def solution(totalPrice, membership, paymentMethod):
    if totalPrice >= 500000:
        answer = totalPrice * 0.85
    elif totalPrice >= 300000:
        answer = totalPrice * 0.9
    elif totalPrice >= 100000:
        answer = totalPrice * 0.95

    if membership == "실버":
        answer = answer * 0.97
    elif membership == "골드":
        answer = answer * 0.95
    elif membership == "플래티넘":
        answer = answer * 0.9
    
    if paymentMethod == "신용카드":
        answer
    elif paymentMethod == "현금":
        answer = answer * 0.98

    if totalPrice >= 500000 and membership == "플래티넘" and paymentMethod == "현금":
        answer = answer - 50000

    return int(answer)
```

# 18번
```
def solution(start, end):
    answer = 0
    for i in range(start, end+1):
        answer += i
    return answer
```

# 19번
```
def solution(start, end):
    answer = 0
    for i in range(start, end+1):
        if i % 2 ==0:
            answer += i
    return answer
```

# 20번
```
def solution(start, end, number):
    answer = 0
    for i in range(start, end+1):
        if i % number ==0:
            answer += i
    return answer
```

---

# 21번
```
def solution(start, end):
    answer = 0
    for i in range(start, end+1):
        is_prime = True
        if i == 1:
            is_prime = False
        else: 
            for a in range(2, i):
                if i % a == 0:
                    is_prime = False
                    break
        if is_prime == True :
            answer += 1
    return answer
```
- `is_prime = True` : 소수입니다. 가정

- for 문 안에 `is_prime = True` 쓰는 이유   
    ex) is_prime = True 를 for 문 밖에 쓰면   
        i = 6, is_prime = False -> 여기서 is_prime = True 가 False 로 재할당됨   
        i = 7, is_prime = False -> is_prime = True 로 재할당 되는 식이 없어서 7이 소수여도 False 가 나타남   

- `for a in range(2, i):` 에서 i+1 이 아니라 i 를 쓰는 이유   
    : i+1 일 경우, for문 맨 마지막이 i ÷ i = 1 로 i가 소수여도 나머지가 0으로 `is_prime = False`로 나옴   

- `break`를 쓰는 이유
    ex) i = 12 이면 `for a in range(2, i):` 이 for문이 
    처음 2로 시작할 때부터 `is_prime = False` 가 나오는데 break 를 안 쓰면 마지막 11까지 나누게 되는 불필요한 실행이 생김

---

# 22번

1. 첫번째 방법 : 문자열로 바꾸기
```
def solution(number):
    answer = str(number)
    return len(answer)
```

2. 두번째 방법 : 10으로 나눈 횟수
```
def solution(number):
    answer = 0
    while number > 0:
        number = number // 10
        answer += 1
    return answer
```

- while 반복문은 조건이 참일 때까지만 반복

---

# 23번 (25.11.13.)
- 내가 푼 식
```
def solution(number):
    answer = str(number)
    sum = 0
    for i in range(0, len(answer)):
        sum += int(answer[i])
    return sum
```
- 더 간단한 방법
```
def solution(number):
    answer = 0
    for i in str(number):
        answer += int(i)
    return answer
```

---

# 24번 (25.11.27)
- 내가 푼 식 (range 쓰는 것 주의)
```
def solution(start, end):
    answer = 0
    for i in range(start, end+1):
        for a in range(1, 10):
            answer += i * a
    return answer
```
- 다른 방법
> 1+2+3+4+5+6+7+8+9 = 45
> 2단의 합 = 2×1+2×2+ ··· +2×9 = 2×(1+2+ ··· +9) = 2 × 45
> 3단의 합 = 3 × 45
> n단의 합  = n × 45
```
def solution(start, end):
    answer = 0
    for i in range(start, end+1):
        answer += i * 45
    return answer
```

---

