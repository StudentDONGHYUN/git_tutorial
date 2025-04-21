# git_tutorial

## 프로젝트 개요
터미널에서 실행되는 간단한 Maple 게임을 구현합니다. 플레이어는 캐릭터를 조작해 몬스터를 사냥하고 경험치를 획득하며 레벨업할 수 있습니다.

## 주요 기능
- characters.ini 파일로부터 캐릭터 능력치 로드
- 캐릭터 목록 표시 및 선택
- 키 입력(w/a/s/d)으로 이동
- 기본 공격(b) 및 스킬(1~5) 사용
- q 입력으로 게임 종료

## 요구사항
- Python 3.7 이상
- 별도 라이브러리 없이 표준 라이브러리만 사용

## 설치 및 실행 방법
```bash
git clone https://github.com/username/maple-terminal-game.git
cd maple-terminal-game
python main.py
```

## 파일 구조
```bash
.
├─ main.py           # 게임 진입점 및 입력 처리
├─ player.py         # 캐릭터 클래스 정의
├─ utils.py          # 캐릭터 구성 파일 로드 함수
└─ characters.ini    # 캐릭터 능력치 설정 파일
```

## 캐릭터 구성 파일 (characters.ini)
INI 포맷으로 캐릭터 능력치를 정의합니다. 예:
```ini
[Warrior]
basic_attack = 10
skill1_attack = 15
...
```

## 사용 방법
1. `python main.py`로 게임 시작  
2. 캐릭터 목록에서 이름 입력  
3. 조작법:  
   - w/a/s/d: 이동  
   - b: 기본공격  
   - 1~5: 각각 스킬 사용  
   - q: 게임 종료

## 향후 개선 사항
- 마을 및 상점 시스템 추가  
- 스킬 및 마법 구현  
- 저장/불러오기 기능  

## 기여
버그 리포트 및 기능 제안은 Issues에 남겨주세요. Pull Request도 환영합니다!