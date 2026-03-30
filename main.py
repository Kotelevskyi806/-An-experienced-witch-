from tarot_core_database import TarotDeck
from tarot_interpretation import get_phrase_by_count
from tarot_reactions import get_random_reaction
from vedunja_generation import get_random_generation
from tarot_question import get_random_question
from tarot_silence import get_silence_reaction

import random
import time
import sys

deck = TarotDeck()
question_count = 0
enter_count = 0

def slow_print(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def interpretation():
    global question_count

    phrase1 = get_phrase_by_count(question_count)
    phrase2 = get_phrase_by_count(question_count)

    while phrase2 == phrase1:
        phrase2 = get_phrase_by_count(question_count)

    slow_print(phrase1)
    slow_print(phrase2)

    print()

    question_count += 1
    slow_print(f"Главное, помни... {get_phrase_by_count(question_count)}")


def draw_card(used_cards):
    available_cards = [card for card in deck.cards.keys() if card not in used_cards]

    card_id = random.choice(available_cards)
    used_cards.add(card_id)

    orientation = random.choice(["upright", "reversed"])
    card = deck.get_card(card_id)

    return card['name'], card[orientation], orientation


def interpret(position, name, meaning, orientation):
    if position == "Прошлое":
        intro = "В прошлом на тебя влияло:"
    elif position == "Настоящее":
        intro = "Сейчас ситуация проявляется так:"
    else:
        slow_print(get_random_reaction())
        print()
        intro = "Так, кхе..кхе... И самое главное - к чему всё движется?:"

    slow_print(intro)

    if position == "Прошлое":
        print()
        slow_print(get_random_reaction())
        print()

    slow_print(f"{name} ({orientation})")
    slow_print(f"{meaning}\n")


def past_present_future():
    positions = ["Прошлое", "Настоящее", "Будущее"]
    used_cards = set()

    slow_print("\nЯ смотрю на карты...")
    print()
    slow_print(get_random_reaction())
    print()

    for pos in positions:
        name, meaning, orientation = draw_card(used_cards)
        interpret(pos, name, meaning, orientation)


slow_print(f"Привет! Я Опытная ведунья в {get_random_generation()} поколении.\n")
slow_print("Не хочу хвастаться, но мои карты видят всё.\n")
slow_print("Чего стоишь? Присаживайся! Я вижу, у тебя ко мне есть вопросы.\n")
slow_print("Ну что, не стесняйся, задавай!\n")

while True:
    raw_input_value = input(f"{get_random_question()} ")
    question = raw_input_value.strip()

    if question == "":
        enter_count += 1

        print()

        if 7 <= enter_count <= 11:
            slow_print("Не стой как столб, мне, конечно, приятно, что ты пришел на меня посмотреть, но...")

        if enter_count == 12:
            slow_print("Ладно, я пошла")
            break

        if enter_count >= 7:
            count = 0
        else:
            count = min(enter_count, 4)

        reactions = set()
        while len(reactions) < count:
            reactions.add(get_silence_reaction())

        for phrase in reactions:
            slow_print(phrase)

        print()
        continue

    if question.lower() == "благодарю и принимаю":
        slow_print("До скорой встречи!")
        break

    enter_count = 0

    print()
    slow_print(f"Так... Значит, твой вопрос: {question}\n")

    past_present_future()
    interpretation()

    slow_print('\nЕсли тебя что-то ещё беспокоит — спрашивай, но если вопросов больше нет, просто напиши "Благодарю и принимаю", и мы закончим сеанс.\n')
