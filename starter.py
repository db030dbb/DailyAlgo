# --------------------
#  1번 : 두 수의 덧셈
# --------------------
def solution(number1, number2):
    answer = number1 + number2
    return answer


# --------------------
#  3번 : 두 수의 뺄셈
# --------------------
def solution(number1, number2):
    answer = number1 - number2
    return answer


# --------------------
#  4번 : 두 수의 곱셈
# --------------------
def solution(number1, number2):
    answer = number1 * number2
    return answer


# --------------------
#  5번 : 두 수의 나눗셈
# --------------------
def solution(number1, number2):
    answer = number1 / number2 * 100
    return int(answer)


# --------------------
#  6번 : 몫 구하기
# --------------------
def solution(number1, number2):
    answer = number1 // number2
    return answer


# --------------------
#  7번 : 나머지 구하기
# --------------------
def solution(number1, number2):
    answer = number1 % number2
    return answer


# --------------------
#  8번 : 거듭제곱
# --------------------
def solution(number, exponent):
    answer = number ** exponent
    return answer


# --------------------
#  9번 : 제곱근 구하기
# --------------------
def solution(number):
    answer = number **0.5
    return int(answer)


# ----------------------------
#  10번 : 두 수의 크기 비교하기
# ----------------------------
def solution(number1, number2):
    if number1 > number2:
        answer = number1
    else:
        answer = number2
    return answer


# --------------------
#  11번 : 짝홀 판별하기
# --------------------
def solution(number):
    if number % 2 == 0 :
        answer = '짝수'
    else:
        answer = '홀수'
    return answer


# --------------------
#  12번 : 부호 판별하기
# --------------------
def solution(number):
    if number > 0:
        answer = "POSITIVE"
    elif number == 0 :
        answer = "ZERO"
    else:
        answer = "NEGATIVE"
    return answer


# ----------------------------
#  13번 : 범위 내 숫자 판별하기
# ----------------------------
def solution(number, start, end):
    if start <= number <= end:
        answer = "YES"
    else:
        answer = "NO"
    return answer


# --------------------
#  14번 : 성적 판별하기
# --------------------
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


# --------------------
#  15번 : 윤년 판별하기
# --------------------
def solution(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        answer = "YES"
    else:
        answer = "NO"
    return answer


# ----------------------
#  16번 : 비만도 계산하기
# ----------------------
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


# ---------------------------
#  17번 : 쇼핑몰 가격 계산하기
# ---------------------------
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


# --------------------------
#  18번 : 범위 내 총합 구하기
# --------------------------
def solution(start, end):
    answer = 0
    for i in range(start, end+1):
        answer += i
    return answer


# ------------------------------
#  19번 : 범위 내 짝수의 합 구하기
# ------------------------------
def solution(start, end):
    answer = 0
    for i in range(start, end+1):
        if i % 2 ==0:
            answer += i
    return answer


# ------------------------------
#  20번 : 범위 내 배수의 합 구하기
# ------------------------------
def solution(start, end, number):
    answer = 0
    for i in range(start, end+1):
        if i % number ==0:
            answer += i
    return answer


# --------------------------------
#  21번 : 범위 내 소수의 개수 구하기
# --------------------------------
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

"""
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
"""


# ---------------------
#  22번 : 자릿수 구하기
# ---------------------

# *** 1. 첫번째 방법 : 문자열로 바꾸기 ***
def solution(number):
    answer = str(number)
    return len(answer)

# *** 2. 두번째 방법 : 10으로 나눈 횟수 ***
def solution(number):
    answer = 0
    while number > 0:
        number = number // 10
        answer += 1
    return answer

# while 반복문은 조건이 참일 때까지만 반복


# ----------------------------
#  23번 : 각 자릿수의 합 구하기
# ----------------------------

# *** 내가 푼 식 ***
def solution(number):
    answer = str(number)
    sum = 0
    for i in range(0, len(answer)):
        sum += int(answer[i])
    return sum

# *** 더 간단한 방법 ***
def solution(number):
    answer = 0
    for i in str(number):
        answer += int(i)
    return answer


# ----------------------------------------
#  24번 : 구구단 결과 합 구하기 (2025.11.27)
# ----------------------------------------

# *** 내가 푼 식 (range 쓰는 것 주의) ***
def solution(start, end):
    answer = 0
    for i in range(start, end+1):
        for a in range(1, 10):
            answer += i * a
    return answer

# *** 다른 방법 ***
"""
> 1+2+3+4+5+6+7+8+9 = 45   
> 2단의 합 = 2×1+2×2+ ··· +2×9 = 2×(1+2+ ··· +9) = 2 × 45   
> 3단의 합 = 3 × 45   
> n단의 합  = n × 45   
"""
def solution(start, end):
    answer = 0
    for i in range(start, end+1):
        answer += i * 45
    return answer


# ------------------------------------------
#  25번 : 모든 약수의 총합 구하기 (2025.11.28)
# ------------------------------------------
# *** 내가 푼 방법 ***
def solution(number):
    answer = 0
    for i in range(1, number+1):
        if i == 1 : 
            answer += 1
        else : 
            for a in range(1,i+1):
                if i % a == 0:
                    answer += a
    return answer

# *** 다른 방법 ***
"""
> number 가 5인 경우에 1은 몇 번 더해지는가? ∴ 5번 (1의 약수, 2의 약수, ··· 5의 약수)   
> 1은 1,2,3,4,5의 약수 -> 5번 (5//1=5)   
> 2은 2,4의 약수 -> 2번 (5//2=2)   
> 3은 3의 약수 -> 1번 (5//3=1)   
> 4은 4의 약수 -> 1번 (5//4=1)   
> 5은 5의 약수 -> 1번 (5//5=1)   
> 따라서 각 숫자 i 는 number // i 번 더해진다.   
"""
def solution(number):
    answer = 0
    for i in range(1, number+1):
        answer += i * (number // i)  
    return answer


# ----------------------------------------
#  26번 : 모든 소수 곱의 총 합 구하기 (2025.11.29)
# ----------------------------------------

# !!! 체감 난이도 상.. 나중에 꼭 다시 풀어보기!(소수 문제 다 다시 풀기) !!!
def solution(start, end):
    primes = []
    for num in range(start, end+1):
        is_prime = True
        if num == 1:
            is_prime = False
        else :
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
        if is_prime == True:
            primes.append(num)
    
    answer = 0
    for a in range(len(primes)):
        for b in range(a+1, len(primes)):
            answer += primes[a] * primes[b]
    return answer


# ----------------------------------------
#  31번 : 문자열의 길이 구하기 (2025.12.02)
# ----------------------------------------
def solution(word):
    answer = len(word)
    return answer


# -------------------------------------------------
#  32번 : 문자열에서 특정 문자 개수 구하기 (2025.12.03)
# -------------------------------------------------
def solution(word, c):
    answer = 0
    for i in range(len(word)):
        if word[i] == c:
            answer += 1
    return answer

# *** 다른 풀이 방법 1 ***
def solution(word, c):
    answer = 0
    for char in word:
        if char == c:
            answer += 1
    return answer

# *** 다른 풀이 방법 2 ***
def solution(word, c):
    return word.count(c)
