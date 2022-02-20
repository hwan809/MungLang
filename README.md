﻿# MungLang
케인인님, -3000딩 한판해요

여러 한국어 esolang들에 영감을 받고,    
스트리머 '[케인](https://www.youtube.com/channel/UC0aKwoKNeqBaUwiEXmkQaGQ)' 님의 밈 중 하나인
[[케인] 무빙맨](https://www.youtube.com/watch?v=92volEdYcCQ) 을 프로그래밍 언어로 구현합니다.

> 다른 언어 구현체 및 리팩토링 PR은 환영입니다! 🙋

    춘잣!
    뭉..코..코..코..코..
    무웅..코.....코..코.....코..코.....코..코.....코.....
    무우웅..코.....코..코.....코..코.....코..
    무우우웅태애앵코~
    무우우우우우웅..코..코..코..코..

    무우우우웅.....코...........
    무우우우우웅~코태애애애앵
    자태앵태애애앵태애애애애앵!
    무우우우웅..코.....코..코.....코.....코.......
    무우우우우웅~코...........
    자태앵태애애애앵태애애애애앵!
    무우우우웅..코.....코..코.....코..코.....
    무우우우우웅..코..코...코.....
    자태앵태애애애앵태애애애애앵!
    무우우우웅..코..코.......코.......
    무우우우우웅~코..코.....코..코.....코..코.....
    자태앵태애애앵태애애애앵태애애애애앵!
    자태애애애애애앵!
    무우우우웅..코.....코..코.....코..코.....
    무우우우우웅..코.....코..코..코..
    자태앵태애애애앵태애애애애앵!
    무우우우웅..코.....코..코.....코..코.....코.....
    무우우우우웅..코..코..코..코..코.....코.....
    무우우우우우우웅..코.....코..코.....코..코.....코..코.....코....
    자태애애애앵태애애애애앵태애애애애애애앵~~~~!
    무우우우웅..코.....코..코.....코..코.....코....
    무우우우우웅..코..코..코..코..
    자태애애애애앵태애애애애애애앵태애애애앵!
    자태애애애애애앵!
    무우우우우우우웅..코.....코..코.....코..코.....코..코.....코.....
    무우우우웅.....코..코.....코..코.....코..
    무우우우우웅~코..코..코..코...
    자태애애애애앵태애애애애애애앵태애애애앵!
    무우우우웅~코..코.....코..코.....코..코.....코...
    무우우우우웅..코..코..코..코.....
    무우우우우웅~태애애애애앵
    무우우우우웅.......코태애애애애앵
    자태애애애애애애앵태애애애앵태애애애애앵!
    무우우우웅.............
    무우우우우웅.....................................
    무우우우우우우우웅~코..코..코...코태애애애앵코태애애애애앵
    자태애애애애애애앵태애애애애애애애앵!
    무우우우웅..코.....코..코.....코...
    무우우우웅~~~~~~~~~태애애애앵
    무우우우웅~코태애애애앵
    자태애애애앵태애애애애애애앵!
    자태애애애애애앵!
    무우우우웅..코..코.....코.....코.....
    자태애애애애애애앵태애애애앵!
    무우우우웅..코..코..코.....코.....코.....
    무우우우우웅..코...코.....코..
    무우우우웅태애애애애앵태애애애앵
    자태애애애애애애앵태애애애앵!
    무우우우웅..코.....코..코.......코.....
    무우우우웅~~~~~~~~~~~~~~~~~태애애애앵
    무우우우웅~코..코..코..코태애애애앵
    자태애애애앵태애애애애애애앵!
    무우우우웅~코..코.....코..코.....코.....코..코.....
    무우우우우웅...코.....코...................
    자태애애애애애애앵태애애애애앵태애애애앵!
    
    ---------------------------------------------
    
    출력 결과 >> 뭉탱이로 있다가 유링계숭 아이그냥

# -3000딩쟁이들을 위한 문법
MungLang(뭉탱어) 의 문법을 서술하는 글이란다.  
간단하니까 무서워하지 말렴! ~~어으 어 어 어떡해 저거~~

## 사용할 수 있는 키워드
 - 뭉
 - 탱
 - 무빙
 - 유링계숭한
 - 아이그냥
 - 춘잣!
 - ~~코~~ -3000
 - 자!
 - 자~
## 자료형
얘! 자료형은 정수밖에 없단다. 귀찮아 임마!
### 정수
정수는 . / ~ 으로 표현이 가능하단다.
```
. => +1
~ => -1
``` 
얘! 곱셈이 잘 안되니? 
케인님의 **코**처럼 불어나는 코 연산자를 쓰렴.

```
..코~~ => 2 * -2 => -4
```
덧셈은 그냥 갖다붙이면 된단다.

## 변수

### 선언 - 뭉
글자 수 번째에 있는 변수에 뒤에 오는 정수를 대입한단다.

```뭉```, ```무웅```, ```무우웅```, ```무우우웅```, ~~```뿌웅 웰컴 투 더 뭉탱이 월드```~~  등을 사용해
글자 수를 증가시킬 수 있단다.

```
무웅~~ => 2번째 변수에 -2 대입
```
### 호출 - 탱
글자 수 번째에 있는 변수를 호출한단다.  
```탱```, ```태앵```, ```태애앵```, ```태애애앵``` 등으로 사용한단다.

```
태애앵 => 3번째 변수
```
## 콘솔
### 출력 - 자!
```를``` 과  ```!``` 사이의 값을 출력한단다.

 - 값이 0 / 없는 경우 => 줄바꿈 조이고 (\n)
 - 값이 양수인 경우 => 그 수에 대응하는 유니코드를 출력 (문자)
 - 값이 음수인 경우 => 절댓값을 출력 (숫자) 

문자를 출력하고 싶니? https://unicodelookup.com/ 참고하렴!
### 입력 - 자~
사용자에게 입력을 받아 준단다.

```
# 입력을 받아 변수에 저장하여 보자
무웅자~ => 2번째 변수에 사용자 입력 저장
```
정수로만 입력하는 게 좋단다!
## (왕간단) 지시문
### 조건문 - 유링계숭한?
뭉탱요정이 **유링계숭한** 힘으로 이것이 케인님의 코인지 판단해 주신단다.  
소원도 같이 빌렴! 케인님의 **코** 라면 소원을 들어주실지도 모른단다.  

```유링계슝한?{변수 또는 정수},{실행할 명령}```
```
# 3번째 변수가 "-3000" 이라면 콘솔에 "2" 출력
유링계숭한?태애앵,자~~! 
```
### GOTO - 무빙
**무빙맨**이 마하 9의 속도로 퀵 서비스를 해 주신단다.
```무빙``` 뒤에 따라오는 정수의 줄 번호로 이동한단다.
```
무빙... => 3번째 줄로 이동
```
### RETURN - 아이그냥
뒤 따라오는 정수를 콘솔 출력 규칙에 따라 출력하고 프로그램을 종료한단다.

## 작성 문법
확장자 : ```.mte```  
프로그램 코드에는 **춘잣!** 으로 프로그램의 시작을 알리렴.  
춘잣! 위의 코드는 컴파일되지 않는단다.

## 예제
이걸로 개발이 잘 안될 거 같니? 가능하단다!
### 구구단 출력
```
춘잣!
뭉..
무웅.
무우웅........
무우우웅...코...
무우우우웅~코...코..........코..........코..........

자~코탱!
자..코..코..코..코..!
자...........코........!
자..코..코..코..코..!
자~코태앵!
자..코..코..코..코..!
자.............................................................!
자..코..코..코..코..!
자~코탱코태앵!
자!
무우우웅태애애앵~
무웅.태앵
유링계숭한?태애애앵태애애애앵,무빙..코...........
무빙..코..코..

뭉.탱
무우웅~태애앵
무우우웅...코...
무웅.
유링계숭한?태애앵태애애애앵,아이그냥!
자!
무빙..코..코..
```
2단부터 구구단을 출력하는 코드란다.

### 컴파일 방법

```
...
git clone https://github.com/hwan809/MungLang.git
cd MungLang
python compiler.py [파일명(examples/gugudan.mte)]
```
![image](https://user-images.githubusercontent.com/55339366/154715252-43a96c8c-9538-4438-9dd5-b65255bc8e09.png)
