import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = {
    "İçime koydukların anı olur, duvardayken şık durur. Çiviyi görünce yaklaştır, ikimiz bir bütün olur.": [
        "ÇERÇEVE",
        "AYAKKABI",
        "MANTI",
        "ISPANAK",
    ],
    "İçi dolu pamuk. Arkanı yaslan, onu doldurduk.": [
        "YASTIK",
        "YORGAN",
        "KANAPE",
        "TOP",
    ],
    "Yer altındadır evi, yersen bitmez lezzeti.": [
        "PANCAR",
        "ENGİNAR",
        "ÇİLEK",
        "AYVA",
    ],
    "Bir kalaylı tas, al duvara as.": [
        "AYNA",
        "ÇERÇEVE",
        "RESİM",
        "TAVA",
    ],
    "Bir bağım var, uzundur uzun.": [
        "SENE",
        "YOL",
        "KÖPRÜ",
        "PATATES",
    ],
    "Kara tavuk dalda yatar, dal kırılır yerde yatar.": [
        "ZEYTİN",
        "AYVA",
        "İNCİR",
        "KARPUZ",
    ],
    "İncecik beli, elimin eli.": [
        "ÇATAL",
        "KAŞIK",
        "KEPÇE",
        "MERDANEA",
    ]
}

num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
questions = random.sample(list(QUESTIONS.items()), k=num_questions)

num_correct = 0
for num, (question, alternatives) in enumerate(questions, start=1):
    print(f"\nSoru {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(
        zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives)))
    )
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nCevap? ")) not in labeled_alternatives:
        print(f"Lütfen {', '.join(labeled_alternatives)} şıkrlarından birini seçin")

    answer = labeled_alternatives[answer_label]
    if answer == correct_answer:
        num_correct += 1
        print("#### !DOĞRU! ####")
    else:
        print("#### !YANLIŞA! ####")
        print(f"{answer!r} cevabı doğru değil, doğru cevap {correct_answer!r} ")

print(f"\n{num} sorudan {num_correct} kadarını doğru cevapladınız")
