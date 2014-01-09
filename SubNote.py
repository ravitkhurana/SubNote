
import sublime
import sublime_plugin
from evernote.api.client import EvernoteClient

class TestCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		print("Hello SubNote!")
