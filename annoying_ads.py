import random
import webbrowser
from prompt_toolkit.shortcuts import button_dialog
from prompt_toolkit.styles import Style

# LINKS IN THE FUNCTIONS

# Rickroll link https://bit.ly/IqT6zt
# PEP8 link https://bit.ly/3ifW7F9       

# change styles according to newspaper
style = Style.from_dict({
    'dialog': 'bg:#a0a0a0',
    'button': 'bg:#bf99a4',
    'dialog.body': 'bg:#a9cfd0',
    'dialog shadow': 'bg:#383838',
    'frame.label': '#fcaca3',
    'dialog.body label': '#fd8bb6',
})


# gonna add few more
def simple_ad() -> None:
    """Calls dialog with content chosen randomly from list inside function"""

    content = [['You won lottery!', 'Congrutulations! To receive 5`000`000$\n'
                                    'at our site, you need to press the button below', 'GET PRIZE'],
               ['Increase your RAM!', 'Limited offer of EnchanceRAM software is now\n'
                                      'at sale with 50% discount! Press the button to open shop', 'MORE RAM'],
               ['Read the fresh news!', 'Your newspaper is outdated! Grab the fresh\n'
                                        'copy at our website for free with 3-day trial! (69$ each month after free '
                                        'trial ends)',
                'FRESH NEWS'],
               ['Join Coffee Club', 'Coffee Club allows you to make money by inviting friends\n'
                                    'and installing Coffee Brewer directly at your GPU!', 'JOIN CLUB'],

               ]
    while True:
        dialog = random.choice(content)
        if button_dialog(
                title=dialog[0],
                text=dialog[1],
                buttons=[
                    (dialog[2], False),
                    ('Close', True),
                ], style=style
        ).run():
            break


def joke_ad() -> None:
    """Calls dialog that can open link in browser if the answer is incorrect"""

    if button_dialog(
            title='Idk',
            text='Do you always follow PEP8?',
            buttons=[
                ('Yes', False),
                ('No', True)],
            style=style).run():
        webbrowser.open('https://bit.ly/3ifW7F9')


def bar_ad() -> None:
    """Calls dialog with bar that need to be filled; can open link in browser"""
    content = ['Fill the bar to close this pop-up!\n', 'Let\'s try over again\n',
               'Just press *tap*, it\'s not so hard\n', 'Feeling rebilous? Just stop pressing "NO"!\n', 'STOP!\n',
               'I warned you!\n', 'Last chance for you to choose right button...']
    counter = 0
    bar = 0
    while True:
        dialog = button_dialog(
            title='Fill the bar!',
            text=f'{content[counter]}[{bar * "==="}>] {bar}//10',
            buttons=random.sample([
                ('*tap*', False),
                ('No', True), ], 2),
            style=style
        )
        if dialog.run():
            bar = 0
            counter += 1
            if counter == len(content):
                webbrowser.open('https://bit.ly/IqT6zt')
                break
        else:
            if counter != 0:
                counter = 0
            bar += 1
            if bar == 10:
                break
