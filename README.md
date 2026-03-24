# 📚 [랭체인으로 구현하는 AI 서비스 & 에이전트 개발 입문] 예제 코드 저장소

본 저장소는 도서의 실습 예제 코드를 담고 있습니다. 
원활한 실습을 위해 아래의 안내에 따라 파이썬 가상환경을 설정하고 필수 패키지를 설치해 주세요.

## ⚙️ 1. 실습 환경 준비 (가상환경 설정)

운영체제와 파이썬 버전에 따른 충돌을 방지하기 위해, 반드시 **가상환경(Virtual Environment)**을 생성하여 실습을 진행하는 것을 권장합니다.

1. **프로젝트 열기:** VS Code에서 다운로드(또는 Clone)한 프로젝트 폴더를 엽니다.
2. **터미널 실행:** 상단 메뉴에서 `Terminal` > `New Terminal`을 클릭하여 터미널 창을 엽니다.
3. **가상환경 생성:** 터미널에 아래 명령어를 입력하여 `venv`라는 이름의 가상환경을 만듭니다.
   ```bash
   python -m venv venv
````

*(※ Mac/Linux 환경에서 `python` 명령어가 작동하지 않는다면 `python3 -m venv venv`를 사용하세요.)*
4\. **가상환경 활성화:** 운영체제에 맞게 아래 명령어를 입력하여 가상환경을 켭니다.

  - **Windows:**
    ```bash
    venv\Scripts\activate
    ```
  - **Mac / Linux:**
    ```bash
    source venv/bin/activate
    ```

> ✅ **확인:** 터미널 입력창 맨 앞에 `(venv)` 표시가 나타났다면 성공입니다\!

<br>

## 📦 2. 필수 패키지 설치

가상환경이 활성화된 상태(`(venv)` 표시 확인)에서, 실습에 필요한 패키지를 한 번에 설치합니다.

```bash
pip install -r requirements.txt
```

<br>

## 🔑 3. 환경 변수 및 API 키 설정 (중요)

이 책의 다양한 LLM(OpenAI, Anthropic, Google) 및 LangSmith(실행 추적) 예제를 실행하려면 아래의 환경 변수 설정이 필요합니다.

**[설정해야 할 변수 목록]**

  * `OPENAI_API_KEY`: OpenAI API 키
  * `ANTHROPIC_API_KEY`: Anthropic API 키
  * `GOOGLE_API_KEY`: Google Gemini API 키
  * `LANGCHAIN_TRACING_V2`: `true` (LangSmith 추적 활성화)
  * `LANGCHAIN_ENDPOINT`: `https://api.smith.langchain.com` (LangSmith 엔드포인트)
  * `LANGCHAIN_API_KEY`: LangSmith API 키

운영체제에 맞게 위 변수들을 설정해 주세요.

  - **Windows 사용자**
    `[제어판 → 시스템 → 고급 시스템 설정 → 환경 변수]` 메뉴로 이동하여 위 목록의 변수들을 각각 **새 시스템 변수**로 추가합니다.

      - 예) 변수 이름: `OPENAI_API_KEY` / 변수 값: `sk-발급받은API키...`

  - **Mac / Linux 사용자**
    터미널에 아래 명령어들을 입력하여 환경 변수를 설정합니다. (발급받은 실제 키 값으로 변경하여 입력하세요.)

    ```bash
    export OPENAI_API_KEY="sk-..."
    export ANTHROPIC_API_KEY="sk-ant-..."
    export GOOGLE_API_KEY="AIzaSy..."
    export LANGCHAIN_TRACING_V2="true"
    export LANGCHAIN_ENDPOINT="[https://api.smith.langchain.com](https://api.smith.langchain.com)"
    export LANGCHAIN_API_KEY="lsv2_pt_..."
    ```

🚨 **[매우 중요] 프로그램 재시작 안내** 🚨
환경 변수를 등록한 후에는 **반드시 실행 중인 VS Code나 터미널 창을 완전히 종료하고 다시 실행**해야 새로운 API 키와 변수 값들이 정상적으로 시스템에 적용됩니다.

<br>

## 🚀 4. 예제 코드 실행 방법

모든 준비가 완료되었습니다\! 각 챕터 폴더로 이동하여 코드를 실행해 보세요.

**일반 파이썬 파일 실행 (.py)**

```bash
python chapter_001/예제파일명.py
```

**스트림릿(Streamlit) 웹 UI 예제 실행**
기본 명령어를 실행하면 `http://localhost:8501` 주소로 웹 브라우저가 열립니다.

```bash
streamlit run chapter_00x/app.py
```

*(※ 만약 책의 안내에 따라 8080 포트로 접속하고 싶거나, 기본 포트가 이미 사용 중이라면 아래와 같이 `--server.port` 옵션을 추가하여 실행해 주세요.)*

```bash
streamlit run chapter_00x/app.py --server.port 8080
```

```

이제 저장소의 첫인상이 될 README 작성이 완벽하게 마무리되었습니다! 

작성된 가이드라인대로 `chapter_001`의 첫 번째 랭체인 예제 코드를 터미널에서 직접 실행해 보면서, 설정이 잘 적용되었는지 함께 테스트해 볼까요?
```