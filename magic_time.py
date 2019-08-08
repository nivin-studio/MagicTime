import sublime
import sublime_plugin
import time
import re

class MagicTimeEncodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for s in self.view.sel():
			if s.empty() or s.size() <= 1:
				break
			
			select_strs = self.view.substr(s)
			settings    = sublime.load_settings('MagicTime.sublime-settings')
			encode_rule = settings.get('encode_rule')

			for rule in encode_rule:
				if re.compile(r'' + rule['regexp'] + '').match(select_strs):
					
					struct_time = time.strptime(select_strs, rule['format'])
					content     = str(int(time.mktime(struct_time)))
					
					self.view.run_command('cut')
					self.view.insert(edit, s.begin(), content)

					break

class MagicTimeDecodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for s in self.view.sel():
			if s.empty() or s.size() <= 1:
				break
			
			select_strs = self.view.substr(s)
			settings    = sublime.load_settings('MagicTime.sublime-settings')
			decode_rule = settings.get('decode_rule')

			for rule in decode_rule:
				if re.compile(r'' + rule['regexp'] + '').match(select_strs):
					
					struct_time = time.localtime(int(select_strs))
					content     = time.strftime(rule['format'], struct_time)

					self.view.run_command('cut')
					self.view.insert(edit, s.begin(), content)
					break

class MagicTimeCreateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for s in self.view.sel():
			if not s.empty() or s.size() > 1:
				self.view.run_command('cut')

			self.view.insert(edit, s.begin(), str(int(time.time())))