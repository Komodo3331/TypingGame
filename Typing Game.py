#  Feel free to edit any part of this game! Just give credits to me, Warhawk947!
# modules
import random
import time
from typing import List
import pygame
import datetime
import math

####################################
#Typing is good for you, you know? #
####################################
print('Warhawk947 proudly presents...')
# info and credits, please read
"""Hello everyone!!
Email: Warhawk947@gmail.com
Youtube Channel: Warhawk947

Song Credits:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Track: MuraD - Run
Music by MuraD
Watch: https://youtu.be/ZgfCOnbLqtQ
Free Download/Stream: https://fanlink.to/muradrun
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
MP3 Link:
https://audiograb.com/C9WGImSI

Follow MuraD:
Instagram:https://www.instagram.com/muradmusic1/
Soundcloud:https://soundcloud.com/murad-baxirli
Youtube :https://www.youtube.com/muradmusic
Enjoy!
"""


# let's start the fun, shall we?
if 'pigs' == 'fly':
    print('pigs can fly' * 1000000000000000000000000000000000000000000000000000000000000000000000000000000)

else:
    print('\n')

# Titles
titles = ['ADMIN', 'Novice', 'Apprentice', 'Master', 'Apprentice Worker', 'Master Worker', 'Ultimate Worker',
          'Apprentice Dreamer', 'Master Dreamer', 'Ultimate Dreamer', 'Experienced', 'Super Experienced',
          'Massively Experienced']

# Jackpots for daily rewards
user_cannot_come_back = False
XP_jackpot = [100, 100, 100, 100, 300, 300, 300, 700, 700, 1500]
event_ticket_jackpot = [1, 1, 1, 1, 3, 3, 3, 7, 7, 15]

# Words!!
EASY_WORDS = '''win   
sit
jet
lie
boy
fan
way
fun
ban
beg
hut
say
map
job
flu
cap
inn
tie
owl
ash
fat
eye
fax
pit
pig
act
can
kid
bat
lay
sea
owe
ice
mud
pie
mix
bar
gun
red
cry'''.split()

MEDIUM_WORDS = '''shout
ready
motif
cower
build
humor
braid
large
grain
smash
tough
pitch
awful
peace
plane
lease
glass
route
right
bread
heavy
piece
grant
adult
dress
thigh
cross
share
glove
cream
laser
scale
worth
pound
spend
spite
youth
north
color
beard'''.split()

HARD_WORDS = '''investment          
functional
convention
resolution
first-hand
gregarious
attachment
reputation
allocation
withdrawal
helicopter
compromise
wilderness
excitement
literature
definition
innovation
microphone
leadership
relinquish
democratic
artificial
motorcycle
reasonable
substitute
human-body
population
relaxation
remunerate
expression
hemisphere
particular
constraint
conscience
possession
systematic
experiment
nomination
depression
earthquake'''.split()


# functions
def add_work_or_sleep(work_or_sleep, num):
    if work_or_sleep == 'work':
        beet_boi = int(save_import['Times Worked'])
        beet_boi += num
        save_import['Times Worked'] = str(beet_boi)

    elif work_or_sleep == 'sleep':
        beet_boi = int(save_import['Times Sleeped'])
        beet_boi += num
        save_import['Times Sleeped'] = str(beet_boi)

    save_game()
    return None


year = month = day = hour = minute = second = 0
x = 0


def get_datetime():
    global year, month, day, hour, minute, second, x
    x = datetime.datetime.now()
    x = str(x)
    x = x.split(' ')

    x[0] = x[0].split('-')
    x[1] = x[1].split(':')
    year = int(x[0][0])
    month = int(x[0][1])
    day = int(x[0][2])
    hour = int(x[1][0])
    minute = int(x[1][1])
    second = math.floor(float(x[1][2]))

    return year, month, day, hour, minute, second


def gain_ticket(num):
    me_and_my_beet = int(save_import['Event Tickets'])
    me_and_my_beet += num
    save_import['Event Tickets'] = str(me_and_my_beet)


owned_titles = []


def check_titles(player_stats, current_word_list):
    #print(int(player_stats['XP']))   Remove later --DONE--

    if not 'Warhawk947' != player_stats['Username']:  # lel i messed with this line a bit
        owned_titles.append(titles[0])

    if current_word_list == EASY_WORDS or MEDIUM_WORDS or HARD_WORDS:
        owned_titles.append(titles[1])

    if current_word_list == MEDIUM_WORDS or HARD_WORDS:
        owned_titles.append(titles[2])

    if current_word_list == HARD_WORDS:
        owned_titles.append(titles[3])

    if int(player_stats['Times Worked']) >= 25:
        owned_titles.append(titles[4])

    if int(player_stats['Times Worked']) >= 75:
        owned_titles.append(titles[5])

    if int(player_stats['Times Worked']) >= 150:
        owned_titles.append(titles[6])

    if int(player_stats['Times Sleeped']) >= 25:
        owned_titles.append(titles[7])

    if int(player_stats['Times Sleeped']) >= 75:
        owned_titles.append(titles[8])

    if int(player_stats['Times Sleeped']) >= 150:
        owned_titles.append(titles[9])

    if int(player_stats['XP']) >= 1500:
        owned_titles.append(titles[10])

    if int(player_stats['XP']) >= 3000:
        owned_titles.append(titles[11])

    if int(player_stats['XP']) >= 6500:
        owned_titles.append(titles[12])


def get_competition_sentences(file_choosen):
    competition_text = []
    with open(file_choosen) as file:
        for line in file:
            line = line.rstrip('\n')
            competition_text.append(line)

        return competition_text


'''
def test_get_competition_sentences():
    x = get_competition_sentences('regular.txt')
    print(x)

while True:
    test_get_competition_sentences()
    break
'''


def run_competition(competition_sentence):
    correct_counter = int(0)
    mistakes = int(0)
    competition_sentence = competition_sentence.split()
    time1 = time.time()
    for counter in range(len(competition_sentence)):
        print('Type \'%s\'' % (competition_sentence[counter]))
        competition_input = input('> ')
        if competition_input == competition_sentence[counter]:
            correct_counter += 1

        else:
            mistakes += 1

    time2 = time.time()
    time3 = time2 - time1
    if mistakes >= 5:
        return 'failed', None

    else:
        return time3, correct_counter


def competition(file_choosen):
    print('Do you want to know how to play this gamemode?')
    beet_power = input('> ')
    if beet_power.strip().lower().startswith('y'):
        hints('competition')
    competition_sentences = get_competition_sentences(file_choosen)
    type_counter = 0
    levels = 0
    for beet in range(len(competition_sentences)):
        print('You will be typing the following text:')
        print('-' * 25)
        print('\n')
        print(competition_sentences[type_counter])
        print('\n')
        print('-' * 25)
        input('Press Enter to begin')
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print('GO!')
        time.sleep(0.3)
        total_time, num_correct = run_competition(competition_sentences[type_counter])
        if total_time == 'failed':
            print('\n')
            print('Oh no! You got more than 5 mistakes! Better luck next time!')
            print('\n')
            time.sleep(2)
            save_game()
            break

        else:
            print('Congratulations!')
            print('You did this round in %s seconds, and got %s correct!' % (total_time, num_correct))
            xp_gain = round((num_correct * 10) - (total_time * 3))
            print('You earned %s XP!' % xp_gain)
            gain_xp(xp_gain)
            save_game()
            levels +=1
            type_counter += 1

    if levels == 11:
        print('Congratulations! You completed this competition! More coming soon!')
        gain_xp(1000)




def hints(gamemode):
    if gamemode == 'sleep':
        print('''
Here is how you play the sleep game mode:
Basically you type 5 words, and for every word you get right, you get one energy, and a bit of XP.
You can use your Energy to work!''')
        input('Press enter to continue!')
        return None

    elif gamemode == 'work':
        print('''
Here is how you play the work game mode
Basically you type 15 words, and you get some XP.
If you get a lot right, you get a lot of XP, but you lose a lot of Energy
On the same note, if you get not a lot right, you don't get a lot of XP, but you don't lose so much Energy.
Also, there may be a chance that you get an event ticket, which you can use once you reach 2000 XP.''')
        return None

    elif gamemode == 'competition':
        print('''
Here is how you COMPETE!
In the competition there are rounds.
In each round you type usually a paragraph of text, word by word.
Get more then 5 mistakes, and you\'re out!
Costs one event ticket.
''')
        return None


def pygame_mixer_initiate():
    pygame.mixer.pre_init()
    pygame.mixer.init()
    pygame.mixer.music.load('MuraD - Run (Official Video).mp3')  # load the music
    # add music!!


def lose_energy(energy_to_use):
    save_import_energy = int(save_import['Energy'])
    save_import_energy -= energy_to_use
    if save_import_energy < 0:
        save_import_energy = 0  # your energy can't be below zero

    save_import_energy = str(save_import_energy)
    save_import['Energy'] = save_import_energy


correct_counter_zero = False


def work(_word_list):
    global correct_counter_zero
    print('You have chosen to c'
          'work')

    print('Would you like instructions on how to play this gamemode?')
    user_choice = input('> ')
    user_choice = user_choice.strip().lower()
    if user_choice.startswith('y'):
        hints('work')

    num_correct, _t_i_m_e_, spam = typing_stimulator(_word_list, 14)  # oof actually 15 words
    print('\n')

    if _t_i_m_e_ == 0:
        correct_counter_zero = True
        _t_i_m_e_ = 1

    if num_correct >= 12:
        print('You had a good day at work, and made %s XP!' % (round(num_correct / (_t_i_m_e_ / 4)) * (num_correct * 4)))
        gain_xp(round(num_correct / (_t_i_m_e_ / 4)) * (num_correct * 4))
        lose_energy(4)
        print('You lost 4 energy')

        get_event_tickets = random.randrange(1, 5) == 2
        if get_event_tickets and save_import['XP'] >= 2000:
            print('Hooray! You got an event ticket! Now you can participate in Competitions!')
            gain_ticket(1)
        time.sleep(0.5)

    elif num_correct >= 5:
        print('You had a OK day at work, and made %s XP, not bad!' % (
                    round(num_correct / (_t_i_m_e_ / 4)) * (num_correct * 4)))
        gain_xp(round(num_correct / (_t_i_m_e_ / 4)) * (num_correct * 4))
        lose_energy(2)
        print('You lost 2 energy')

        get_event_tickets = random.randrange(1, 8) == 5
        if get_event_tickets and save_import['XP'] >= 2000:
            print('Hooray! You got an event ticket! Now you can participate in Competitions!')
            gain_ticket(1)

        time.sleep(0.5)

    else:
        if correct_counter_zero:
            print('You had a terrible day. Try again some other time!')
            gain_xp(0)
            lose_energy(1)
            print('You lost 1 energy')
            time.sleep(0.5)
            save_game()
            return None

        print('You had a bad day and only made %s XP, try again some other time!' % (
                    round(num_correct / (_t_i_m_e_ / 4)) * (num_correct * 4)))
        gain_xp(round(num_correct / (_t_i_m_e_ / 4)) * (num_correct * 4))
        lose_energy(1)
        print('You lost 1 energy')
        time.sleep(0.5)

    save_game()


def choose_list_to_use():
    if int(save_import['XP']) <= 350:
        return EASY_WORDS

    elif int(save_import['XP']) >= 351:
        return MEDIUM_WORDS

    elif int(save_import['XP']) >= 1620:
        return HARD_WORDS

    else:
        return HARD_WORDS


words_to_append_counter = 0


def typing_stimulator(word_list, word_count):
    global words_to_append_counter
    words = []
    for words_to_append_counter in range(word_count + 1):
        words.append(random.choice(word_list))

    input('Press Enter to begin')
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('GO!')
    time.sleep(0.3)

    time1 = time.time()
    correct_counter = 0
    incorrect_counter = 0
    for words_to_output_counter in range(len(words)):
        print('Type \'%s\'' % (words[words_to_output_counter]))
        current_word = input('> ')
        if current_word == words[words_to_output_counter]:
            correct_counter += 1
        else:
            incorrect_counter += 1
    time2 = time.time()
    time3 = time2 - time1
    time3 = round(time3)
    print('Congratulations! You got %s/%s in %s seconds!' % (correct_counter, len(words), time3))
    time.sleep(0.6)
    return correct_counter, time3, incorrect_counter


def sleep(word_list):
    print('\n')
    print('You have chosen to sleep.')

    print('Would you like instructions on how to play this gamemode?')
    user_choice = input('> ')
    user_choice = user_choice.strip().lower()
    if user_choice.startswith('y'):
        hints('sleep')

    correct_counter, _t_im_e_, dont_need_this_lel = typing_stimulator(word_list, 4)  # oof it's actually 5 words lel

    gain_xp(correct_counter)

    save_import_energy = int(save_import['Energy'])
    save_import_energy += correct_counter
    if save_import_energy > 10:
        save_import_energy = 10

    save_import_energy = str(save_import_energy)
    save_import['Energy'] = save_import_energy

    print('You now have %s Energy' % save_import['Energy'])
    input('Press Enter to Continue...')
    save_game()


def gain_xp(correct):
    save_import['XP'] = int(save_import['XP']) + correct


def get_save():
    list_save = {}
    with open('DO_NOT_CHANGE.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            current_save = line.split(',')
            list_save[current_save[0]] = current_save[1]
            # print(current_save)
        # print(list_save)
        if list_save == {'save':'none'}:
            return 'no save'
        return list_save


def save_game():
    print('SAVING...')
    with open('DO_NOT_CHANGE.txt', 'w') as file:  # change 'a' back to 'w' when done!! --DONE--
        for key in save_import:
            file.write('%s,%s' % (key, save_import[key]))
            file.write('\n')


def tutorial():
    print('This is the typing stimulator, where you get better and better at typing!')
    time.sleep(1)
    print('''A typical typing match would look like this:

Type 'Dog' 
> Dog
Type 'Cool'
> Cool
etc.
Congratulations! You got 10/10 right in 35 seconds!
+ 100 XP
etc.''')
    print('Make sure you know everything, then press enter.')
    input('Press enter!')

    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('GO!')
    time.sleep(0.3)
    _w_o_rd_s_ = []
    for x in range(1, 11):
        _w_o_rd_s_.append(random.choice(EASY_WORDS))
    time1 = time.time()
    correct_counter = 0
    for x in range(len(_w_o_rd_s_)):
        print('Type \'%s\'' % (_w_o_rd_s_[x]))
        current_word = input('> ')
        if current_word == _w_o_rd_s_[x]:
            correct_counter += 1
    time2 = time.time()
    time3 = time2 - time1
    print('Congratulations! You got %s/10 right in %s seconds!' % (correct_counter, round(time3)))
    time.sleep(3)
    print('%s seconds! That\'s some speed!' % (round(time3)))
    print('Here is some XP!')
    gain_xp(correct_counter)
    # print(correct_counter)
    save_import['Tutorial Passed'] = 'Yes'
    print('You now have %s XP' % (save_import['XP']))
    save_game()


##########
# Start  #
# Screen #
##########


pygame_mixer_initiate()  # whew all this code i'm tired lel
pygame.mixer.init()
pygame.mixer.music.play(-1)

while True:
    print('Typing Game [Alpha Release]')
    print('Do you want to start a [N]ew Game , or [C]ontinue from Save?')
    start_option = input('> ')
    start_option = start_option.strip().lower()

    if start_option == 'n':
        print('Are you sure you want to start over? (Y/N)')
        start_over = input('> ')
        start_over = start_over.strip().lower()
        if start_over == 'y':
            print('Alrighty!')
            time.sleep(0.6)

            print('So... What\'s your name?')
            time.sleep(0.5)

            print('(Hint: type when this prompt shows \'> \')')
            name = input('> ')

            if name.strip() is None or name.strip() == '':
                while name.strip() is None or name.strip() != '':
                    print('''Your username CAN NOT be nothing!
Please try again next time.''')
                    break
            else:

                time.sleep(0.3)
                print('Well, hello there %s!' % name)
                save_import = {'Username': name, 'Chosen Title': 'None',
                               'Titled Username': 'None', 'XP': '0', 'Energy': '10', 'Event Tickets': '0',
                               'Tutorial Passed': 'No', 'Competition Stage': '0', 'Title': 'None',
                               'Times Worked': '0', 'Times Sleeped': '0', 'Date': 'None'}  # reset stats
                save_game()
                print('So...')
                time.sleep(0.7)
                print('Now that we\'ve got your account all nice and tidy, now let\'s move on the the Real Fun...')
                time.sleep(1.1)
                print('...THE TYPING!!!!')
                time.sleep(0.9)
                tutorial()
                break

        else:
            print('CANCELLED.')
            time.sleep(1)
            print('\n')
            continue

    elif start_option == 'c':
        print('\n')
        print('Loading...')
        save_import = get_save()  # get the save info
        if save_import == 'no save':
            print('You haven\'t started a game yet. Try making a new game')
            print('\n')
            continue

        break

    else:
        print('Invalid Key')
        print('\n')

##################
# GAME|GAME|GAME #
# MAIN SCRIPT    #
##################


if save_import['Titled Username'] != 'None':
    print('Welcome back, %s!' % save_import['Titled Username'])

else:
    print('Welcome back, %s!' % save_import['Username'])

WORD_LIST = choose_list_to_use()
check_titles(save_import, WORD_LIST)
# print(owned_titles)

while True:
    print('\n')
    estimated_titles = owned_titles
    owned_titles = []
    check_titles(save_import, WORD_LIST)

    # print(estimated_titles)
    # print(owned_titles)

    if estimated_titles != owned_titles:
        print('You have a new Title! Check your settings for the new Title.')
        print('\n')
        time.sleep(1)

    print('You have %s energy' % save_import['Energy'])
    DIFFICULTY = WORD_LIST
    # save_import['XP'] = '5000'
    WORD_LIST = choose_list_to_use()
    if DIFFICULTY != WORD_LIST:
        print('\n')
        print('Congratulations! You have leveled up to a different word list!')
        print('--------------------------------------')
        print('\n')
        print('Do you want to see Technical Information?')
        choice = input('(Y/N)> ')
        if choice.strip().lower().startswith('y'):
            print('TECHNICAL INFORMATION:')
            print('ORIGINAL LIST = %s' % DIFFICULTY)
            print('NEW LIST = %s' % WORD_LIST)
        save_game()
    print('What would you like to do?')
    if int(save_import['XP']) >= 2000:
        print('Would you like to [W]ork, [S]leep, [C]ompete, go to S[e]ttings, or collect your [D]aily Reward?')

    else:
        print('Would you like to [W]ork, [S]leep, go to S[e]ttings, or collect your [D]aily Reward? ')

    user_option = input('> ')

    user_option = user_option.strip().lower()

    if user_option.startswith('w'):
        if int(save_import['Energy']) != 0:
            work(WORD_LIST)
            add_work_or_sleep('work', 1)

        else:
            print('Sorry, but you\'re out of energy. Try sleeping!')

    elif user_option.startswith('s'):
        sleep(WORD_LIST)
        add_work_or_sleep('sleep', 1)

    elif user_option.startswith('c'):
        if int(save_import['XP']) >= 2000:
            if int(save_import['Event Tickets']) != 0:
                gain_ticket(-1)
                save_game()
                competition('regular.txt')  # switch to more options later
                save_game()

            else:
                print('You don\'t have any event tickets. Try again when you have them.')
                continue

        else:
            print('Invalid Option')
            continue

    elif user_option.startswith('e'):
        while True:
            print('Welcome to settings. Where do you want to go?')
            print('[C]hange Username, [S]ound options, [T]itles, or [E]xit?')
            user_option_nope = input('> ')
            user_option_nope = user_option_nope.strip().lower()
            if user_option_nope.startswith('c'):
                print('CHANGE USERNAME')
                print('\n')
                print('What do you want your new username to be?')
                user_option_nope_yep = input('> ')
                save_import['Username'] = user_option_nope_yep
                print('Your new username is %s' % user_option_nope_yep)

                # update titled name as well if user has one

                if save_import['Chosen Title'] is not None:
                    save_import['Titled Username'] = '%s %s' % (save_import['Chosen Title'], user_option_nope_yep)

                save_game()

                time.sleep(2)
                continue

            elif user_option_nope.startswith('s'):
                if pygame.mixer_music.get_volume() == 0:
                    print('Do you want to Un-Mute the song?')
                    user_option_nope_yep_maybe = input('> ')
                    if user_option_nope_yep_maybe.lower().strip().startswith('y'):
                        pygame.mixer_music.set_volume(1)
                        continue

                if pygame.mixer_music.get_volume() != 0:
                    print('Do you want to Mute the song?')
                    user_option_nope_yep_maybe = input('> ')
                    if user_option_nope_yep_maybe.lower().strip().startswith('y'):
                        pygame.mixer_music.set_volume(0)
                        continue

            elif user_option_nope.startswith('t'):
                triggered = 'not yet'
                print('Welcome to the Titles Section.')
                print('Right now the titles you have are: ')
                for i_love_beets in range(len(owned_titles)):
                    print(i_love_beets, owned_titles[i_love_beets])

                while True:
                    error = 'pending'
                    # print(error)
                    print('Which one would you like to use? Use the number located to the left of the title.')
                    user_option_nope_yep_nope_yep = input('> ')

                    try:
                        user_option_nope_yep_nope_yep = int(user_option_nope_yep_nope_yep)
                    except ValueError:
                        error = 'triggered'

                    if error != 'triggered':
                        if user_option_nope_yep_nope_yep + 1 > int(len(owned_titles)):
                            print('Invalid choice.')

                    elif error == 'triggered':
                        print('Invalid choice')

                    else:
                        choosen_title = owned_titles[user_option_nope_yep_nope_yep]
                        save_import['Titled Username'] = '[%s] %s' % (choosen_title, save_import['Username'])
                        print('Your name is now %s.' % save_import['Titled Username'])
                        save_game()
                        break

            elif user_option_nope.startswith('e'):
                print('Leaving Settings...')
                time.sleep(0.3)
                break

            else:
                print('Invalid Choice.')
                print('\n')

    elif user_option.startswith('d'):
        year, month, day, hour, minute, second = get_datetime()
        x = save_import['Date'].split(' ')
        user_passed = 'Pending'

        if x[0] == 'None':
            x = save_import['Date'] = '%s %s %s %s %s %s' % (year, month, day, hour, minute, second)
            save_game()
            user_passed = True

        elif not user_passed or user_passed == 'Pending' or user_cannot_come_back:
            if int(x[2]) == int(day):
                user_passed = False

            elif int(x[2]) != int(day):
                user_passed = True


        # print(x)
        # print(day)

        if user_passed:
            print('Everyone\'s favorite part of their day, DAILY REWARDS!')
            time.sleep(0.2)
            input('Press enter to spin!')
            print('Spinning...')
            x = random.SystemRandom()  # to make things easier
            y = x.randrange(1, 3)
            if y == 1:
                reward_pass = 'XP'
            else:
                reward_pass = 'event ticket(s)'

            if reward_pass == 'XP':
                z = XP_jackpot

            else:
                z = event_ticket_jackpot

            x.shuffle(z)
            z = z[0]
            if reward_pass == 'XP':
                gain_xp(int(z))

            else:
                gain_ticket(int(z))

            print('\n')
            print('-' * 25)
            print('You received %s %s!' % (z, reward_pass))
            print('-' * 25)
            time.sleep(2)

            save_game()
            print('Come back tomorrow for more exciting prizes!')
            time.sleep(0.2)
            user_cannot_come_back = True
            continue

        else:
            print('You\'ve already collected your Daily Reward, come back tomorrow!')

    else:
        print('Invalid Option')
