import sys
import re

file_path = './input.txt'

def total_scratchcard_count(input_file):
    cards_with_count = list()
    with open(input_file, 'r') as file:
        for line in file:
            card_num, scratch_nums = line.split(':')
            card = {"copies": 1, "card": scratch_nums.strip()}
            cards_with_count.append(card)
        for card_num, card in enumerate(cards_with_count):
            # print(card_num, card)
            winning, owned = card["card"].split('|')
            win_list = winning.split()
            own_list = owned.split()
            for _ in range(card["copies"]):
                wins = 0
                for number in own_list:
                    if number in win_list:
                        wins += 1
                        if card_num + wins >= len(cards_with_count):
                            cards_with_count[-1]["copies"] += 1
                        else:
                            # print(cards_with_count[card_num + wins])
                            cards_with_count[card_num + wins]["copies"] += 1
        total_card_count = sum(card["copies"] for card in cards_with_count)
        return f'The total number of scratchcards with copies is {total_card_count}.'


def total_scratchcard_points(input_file):
    sum = 0
    with open(input_file, 'r') as cardlist:
        for card in cardlist:
            card_worth = 0
            _, numbers = card.split(':')
            winning, owned = numbers.split('|')
            win_list = winning.split()
            own_list = owned.split()
            for number in own_list:
                if number in win_list and card_worth == 0:
                    card_worth = 1
                elif number in win_list:
                    card_worth *= 2
            sum += card_worth

    return f'The scratchcards are worth {sum} points in total.'


input_file = file_path
print(total_scratchcard_count(input_file))