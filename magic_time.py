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
				try:
					struct_time = time.strptime(select_strs, rule)
					content     = str(int(time.mktime(struct_time)))

					self.view.run_command('cut')
					self.view.insert(edit, s.begin(), content)
					print('encode succeed')
					break
				except Exception as e:
					print('encode fail:' + rule)
					continue

class MagicTimeDecodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for s in self.view.sel():
			if s.empty() or s.size() <= 1:
				break
			
			select_strs   = self.view.substr(s)
			settings      = sublime.load_settings('MagicTime.sublime-settings')
			decode_format = settings.get('decode_format')

			try:
				struct_time = time.localtime(int(select_strs))
				content     = time.strftime(decode_format, struct_time)

				self.view.run_command('cut')
				self.view.insert(edit, s.begin(), content)
				print('decode succeed')
				break
			except Exception as e:
				print('decode fail')
				break

class MagicTimeCreateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for s in self.view.sel():
			if not s.empty() or s.size() > 1:
				self.view.run_command('cut')
				
			self.view.insert(edit, s.begin(), str(int(time.time())))