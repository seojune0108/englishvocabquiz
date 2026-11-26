import random

# 난이도별 영단어 데이터 (딕셔너리와 리스트 구조)
VOCAB_DATA = {
    1: {  # 쉬움
        "abundant": "풍부한",
        "essential": "필수적인",
        "frequent": "빈번한",
        "obvious": "명백한",
    },
    2: {  # 보통
        "ambiguous": "모호한",
        "compensate": "보상하다",
        "inevitable": "피할 수 없는",
        "reluctant": "꺼리는",
    },
    3: {  # 약간 어려움
        "coherent": "일관성 있는",
        "deteriorate": "악화되다",
        "fluctuate": "변동하다",
        "vulnerable": "취약한",
    },
    4: {  # 어려움
        "alleviate": "완화하다",
        "contemplate": "심사숙고하다",
        "exacerbate": "악화시키다",
        "ubiquitous": "어디에나 있는",
    },
    5: {  # 매우 어려움
        "acquiesce": "묵인하다",
        "ephemeral": "수명이 짧은, 덧없는",
        "obfuscate": "애매하게 만들다",
        "recalcitrant": "완강히 저항하는",
    },
}

# 오답 보기를 만들기 위해 모든 뜻을 하나의 리스트에 모으기 (for 반복문 활용)
all_meanings = []
for level_dict in VOCAB_DATA.values():
    for meaning in level_dict.values():
        all_meanings.append(meaning)

print("=== 📚 고등학생 필수 영단어 객관식 퀴즈 ===")

# 1. 올바른 난이도를 입력할 때까지 반복 (while 반복문 + if/elif/else 조건문)
while True:
    print("\n[난이도 선택]")
    print("1: 쉬움 | 2: 보통 | 3: 약간 어려움 | 4: 어려움 | 5: 매우 어려움")
    user_input = input("원하는 난이도 번호를 입력하세요 (1~5): ")

    if user_input == "1":
        level = 1
        level_name = "쉬움"
        break
    elif user_input == "2":
        level = 2
        level_name = "보통"
        break
    elif user_input == "3":
        level = 3
        level_name = "약간 어려움"
        break
    elif user_input == "4":
        level = 4
        level_name = "어려움"
        break
    elif user_input == "5":
        level = 5
        level_name = "매우 어려움"
        break
    else:
        print("⚠️ 잘못된 입력입니다. 1부터 5 사이의 숫자만 입력해주세요.")

print(f"\n[{level_name}] 난이도 퀴즈를 시작합니다!\n" + "-" * 40)

# 선택한 난이도의 단어들을 리스트로 가져와 무작위로 섞기
quiz_words = list(VOCAB_DATA[level].items())
random.shuffle(quiz_words)

score = 0  # 맞힌 개수 저장

# 2. 문제 출제 반복문 (for 반복문 활용)
for question_num, (word, correct_meaning) in enumerate(quiz_words, start=1):
    # 오답 3개 뽑기 (while 반복문과 if 조건문으로 중복 방지)
    options = [correct_meaning]
    while len(options) < 4:
        random_meaning = random.choice(all_meanings)
        if random_meaning not in options:
            options.append(random_meaning)

    random.shuffle(options)  # 보기 순서 섞기

    # 문제 및 4지선다 출력 (for 반복문 활용)
    print(f"문제 {question_num}. '{word}'의 뜻으로 알맞은 것은?")
    for idx in range(4):
        print(f"  {idx + 1}) {options[idx]}")

    # 3. 사용자 정답 입력 및 유효성 검사 (while 반복문 + if 조건문)
    while True:
        answer = input("정답 번호 (1~4): ")
        if answer in ["1", "2", "3", "4"]:
            selected_meaning = options[int(answer) - 1]
            break
        else:
            print("⚠️ 1~4 사이의 번호를 입력해주세요.")

    # 4. 정답 판별 (if / else 조건문)
    if selected_meaning == correct_meaning:
        print("⭕ 정답입니다!\n")
        score += 1
    else:
        print(f"❌ 오답입니다. 정답은 '{correct_meaning}'입니다.\n")

# 5. 최종 결과 및 등급 출력 (if / elif / else 조건문)
total = len(quiz_words)
print("-" * 40)
print(f"퀴즈 종료! 총 {total}문제 중 {score}문제를 맞혔습니다.")

if score == total:
    print("🏆 완벽합니다! 해당 난이도를 마스터했어요.")
elif score >= total / 2:
    print("👍 잘했습니다! 틀린 단어만 한 번 더 복습해보세요.")
else:
    print("💪 조금 더 복습이 필요해요. 다시 도전해보세요!")
