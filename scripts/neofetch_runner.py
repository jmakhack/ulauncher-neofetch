from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.event import KeywordQueryEvent

import subprocess
from os import environ

class KeywordQueryEventListener(EventListener):
    def on_event(self, _, extension):
        terminal = extension.preferences['neofetch-terminal']
        param = extension.preferences['neofetch-executing-parameter']
        shell = environ['SHELL']
        subprocess.run([f'{terminal} {param} {shell} -c "neofetch; {shell}"'], shell=True)
        return HideWindowAction()

class NeofetchRunner(Extension):
    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
