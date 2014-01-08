
import sublime, sublime_plugin

class TestCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		print("Hello SubNote!")
