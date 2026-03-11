# KOFA Recruit Alert

한국영상자료원(KOFA) 채용 공고 페이지에 새 글이 올라오면 자동으로 이메일 알림을 보내는 GitHub Actions 기반 모니터링 프로젝트.

## Overview

이 프로젝트는 다음 과정을 자동으로 수행한다.

1. GitHub Actions가 일정 주기로 실행됨
2. KOFA 채용 공고 페이지를 크롤링
3. 가장 최신 게시글을 확인
4. 이전에 저장된 게시글과 비교
5. 새 공고가 발견되면 이메일로 알림 발송

서버 없이 GitHub Actions만으로 동작하는 간단한 자동화 프로젝트다.

---

## Monitored Page

KOFA 채용 공고 페이지

https://www.koreafilm.or.kr/kofa/news/recruit

---

## Project Structure

```
kofa-recruit-alert
├ monitor.py
├ last_post.txt
└ .github
    └ workflows
        └ check.yml
```

설명

monitor.py
→ 채용 공고 페이지 크롤링 및 새 게시글 감지

last_post.txt
→ 마지막으로 확인한 게시글 제목 저장

check.yml
→ GitHub Actions 워크플로우 (자동 실행)

---

## How It Works

1. GitHub Actions가 스케줄에 따라 실행
2. monitor.py가 KOFA 채용 페이지 요청
3. 최신 게시글 제목 추출
4. last_post.txt와 비교
5. 새로운 게시글이면 이메일 발송
6. last_post.txt 업데이트

---

## GitHub Actions Schedule

현재 설정

```
cron: "0 * * * *"
```

의미

매 1시간마다 실행

필요하면 다음과 같이 변경 가능

```
10분마다
*/10 * * * *

하루 1번
0 9 * * *
```

---

## Email Notification Setup

이 프로젝트는 SMTP를 이용해 이메일을 전송한다.

### 1. GitHub Secrets 설정

Repository → Settings → Secrets and variables → Actions

다음 세 개 추가

EMAIL_ID
보내는 이메일 주소

EMAIL_PW
SMTP 앱 비밀번호

EMAIL_TO
알림 받을 이메일 주소

예시

```
EMAIL_ID = your_email@naver.com
EMAIL_PW = smtp_app_password
EMAIL_TO = your_email@naver.com
```

---

### 2. Naver SMTP 설정

네이버 메일 기준

SMTP 서버

```
smtp.naver.com
port: 465
```

네이버 계정

1. 2단계 인증 활성화
2. 앱 비밀번호 생성
3. 생성된 비밀번호를 EMAIL_PW에 입력

---

## Workflow Trigger

워크플로우는 두 가지 방식으로 실행 가능하다.

### 자동 실행

GitHub Actions 스케줄에 따라 자동 실행

### 수동 실행

GitHub → Actions → Run workflow

---

## Test Method

메일 알림 테스트 방법

1. last_post.txt 열기
2. 내용을 임의 텍스트로 변경

예

```
test
```

3. GitHub Actions 실행

그러면 새로운 게시글로 인식하여 이메일이 발송된다.

---

## Example Notification

메일 예시

```
Subject: KOFA 채용 공고 알림

새 채용 공고 올라옴

게시글 제목
https://www.koreafilm.or.kr/...
```

---

## Tech Stack

Python
BeautifulSoup
Requests
GitHub Actions
SMTP Email

---

## Future Improvements

가능한 확장 아이디어

여러 채용 사이트 동시 모니터링
텔레그램 알림 추가
Discord 알림 추가
RSS 피드 생성
웹 대시보드 구축

---

## License

MIT License
