# 📚 랭체인으로 구현하는 AI 서비스 & 에이전트 개발 입문

<p align="left">
  <img src="https://www.youngjin.com/images/book_cover/9788931482850.jpg" height="350px" style="border: 1px solid grey;">
</p>

본 저장소는 도서의 실습 예제 코드를 담고 있습니다.
원활한 실습을 위해 아래 안내에 따라 파이썬 가상환경을 설정하고 필수 패키지를 설치해 주세요.

---

## ⚙️ 1. 실습 환경 준비 (가상환경 설정)

운영체제와 파이썬 버전에 따른 충돌을 방지하기 위해, 반드시 **가상환경(Virtual Environment)** 을 생성하여 실습을 진행하는 것을 권장합니다.

**1단계 — 프로젝트 열기**
VS Code에서 다운로드(또는 Clone)한 프로젝트 폴더를 엽니다.

**2단계 — 터미널 실행**
상단 메뉴에서 `Terminal` > `New Terminal`을 클릭합니다.

**3단계 — 가상환경 생성**

```bash
python -m venv venv
```

> ※ Mac/Linux에서 `python` 명령어가 작동하지 않으면 `python3 -m venv venv`를 사용하세요.

**4단계 — 가상환경 활성화**

| 운영체제 | 명령어 |
|---|---|
| Windows | `venv\Scripts\activate` |
| Mac / Linux | `source venv/bin/activate` |

> ✅ 터미널 입력창 앞에 `(venv)` 표시가 나타나면 성공입니다!

---

## 📦 2. 필수 패키지 설치

가상환경이 활성화된 상태에서 아래 명령어를 실행합니다.

```bash
pip install -r requirements.txt
```

---

## 🔑 3. 환경 변수 및 API 키 설정

다양한 LLM(OpenAI, Anthropic, Google) 및 LangSmith 예제를 실행하려면 아래 환경 변수 설정이 필요합니다.

| 변수명 | 설명 |
|---|---|
| `OPENAI_API_KEY` | OpenAI API 키 |
| `ANTHROPIC_API_KEY` | Anthropic API 키 |
| `GOOGLE_API_KEY` | Google Gemini API 키 |
| `LANGCHAIN_TRACING_V2` | `true` (LangSmith 추적 활성화) |
| `LANGCHAIN_ENDPOINT` | `https://api.smith.langchain.com` |
| `LANGCHAIN_API_KEY` | LangSmith API 키 |

**Windows**

`제어판 → 시스템 → 고급 시스템 설정 → 환경 변수`에서 위 변수들을 새 시스템 변수로 추가합니다.

**Mac / Linux**

```bash
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
export GOOGLE_API_KEY="AIzaSy..."
export LANGCHAIN_TRACING_V2="true"
export LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
export LANGCHAIN_API_KEY="lsv2_pt_..."
```

> 🚨 **중요:** 환경 변수 등록 후에는 VS Code와 터미널을 완전히 종료하고 다시 실행해야 변경 사항이 적용됩니다.

---

## 🚀 4. 예제 코드 실행

**일반 파이썬 파일**

```bash
python chapter_001/예제파일명.py
```

**Streamlit 웹 UI 예제**

```bash
streamlit run chapter_00x/app.py
```

브라우저에서 `http://localhost:8501`로 자동 접속됩니다.

포트를 변경하려면 `--server.port` 옵션을 추가하세요.

```bash
streamlit run chapter_00x/app.py --server.port 8080
```
