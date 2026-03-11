# KOFA Recruit Alert

한국영상자료원(KOFA) 채용 공고를 자동으로 모니터링하고 새로운 공고가 올라오면 이메일로 알림을 보내는 자동화 프로젝트입니다.

GitHub Actions를 이용해 정기적으로 채용 페이지를 확인하고, 변경 사항이 있을 경우 메일을 발송합니다.
또한 채용 공고 목록을 jobs.json에 저장하고 GitHub Pages를 통해 웹페이지에서도 확인할 수 있습니다.

---

## 주요 기능

* KOFA 채용 페이지 자동 크롤링
* 새로운 채용 공고 감지
* 이메일 알림 발송 (SMTP)
* 채용 공고 목록 자동 업데이트 (jobs.json)
* GitHub Pages를 통한 채용 공고 리스트 웹페이지 제공
* GitHub Actions 기반 자동 실행 (1시간마다)

---

## 프로젝트 구조

```
kofa-recruit-alert
│
├ monitor.py              # 채용 공고 크롤링 및 알림 스크립트
├ jobs.json               # 채용 공고 데이터 저장
├ last_post.txt           # 마지막 확인 공고 기록
├ index.html              # 채용 공고 웹페이지
│
└ .github
    └ workflows
        └ check.yaml      # GitHub Actions 자동 실행 설정
```

---

## 동작 흐름

```
GitHub Actions 실행
↓
monitor.py 실행
↓
KOFA 채용 페이지 크롤링
↓
새 공고 확인
↓
jobs.json 업데이트
↓
이메일 알림 발송
↓
GitHub Pages 웹사이트 자동 반영
```

---

## 실행 주기

GitHub Actions cron 설정

```
0 * * * *
```

1시간마다 채용 페이지를 확인합니다.

또한 workflow_dispatch를 통해 수동 실행도 가능합니다.

---

## 환경 변수 설정

GitHub Repository → Settings → Secrets → Actions

다음 값을 추가해야 합니다.

```
EMAIL_ID   : 발신 이메일
EMAIL_PW   : 이메일 SMTP 비밀번호
EMAIL_TO   : 수신 이메일
```

예시

```
EMAIL_ID = example@gmail.com
EMAIL_PW = app_password
EMAIL_TO = example@gmail.com
```

---

## 웹페이지

GitHub Pages를 통해 채용 공고 목록을 확인할 수 있습니다.

```
https://suheon99.github.io/kofa-recruit-alert/
```

웹페이지에서는 jobs.json 데이터를 기반으로 채용 공고 리스트를 보여줍니다.

---

## 기술 스택

Python
Requests
BeautifulSoup
GitHub Actions
GitHub Pages

---

## 목적

이 프로젝트는 다음과 같은 자동화 경험을 위해 제작되었습니다.

* 웹 크롤링
* GitHub Actions 자동화
* 이메일 알림 시스템
* 정적 웹페이지 배포
* 데이터 파이프라인 기초 구현

채용 공고를 수동으로 확인하는 번거로움을 줄이고 자동으로 알림을 받을 수 있도록 하는 것이 목표입니다.
