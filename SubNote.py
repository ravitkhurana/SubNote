import traceback
import subprocess
import sublime
import sublime_plugin

class TestCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		print("Hello SubNote!")
		self.caller()
		print("Bye SubNote")

	def caller(self):
		command = ["python", "./evernote_test/evernote_test.py"]
		try:
			err_file = open("error.log", 'w')
			output = subprocess.check_output(command, universal_newlines=True, stderr=err_file)
		except:
			traceback.print_exc(file=sys.stdout)
			output = "Error Occured."

		print(output)
		
