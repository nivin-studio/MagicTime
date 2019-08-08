import sublime
import sublime_plugin
import time
import re

class MagicTimeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for s in self.view.sel():
			if s.empty() or s.size() <= 1:
				break
			strs = self.view.substr(s)

			type1 = re.compile(r'^[0-9]+$')
			type2 = re.compile(r'^([1-9][0-9][0-9][0-9])-(0?[1-9]|1[0-2])-(0?[1-9]|1[0-9]|2[0-9]|3[0-1])$')
			type3 = re.compile(r'^([1-9][0-9][0-9][0-9])/(0?[1-9]|1[0-2])/(0?[1-9]|1[0-9]|2[0-9]|3[0-1])$')
			type4 = re.compile(r'^([1-9][0-9][0-9][0-9])年(0?[1-9]|1[0-2])月(0?[1-9]|1[0-9]|2[0-9]|3[0-1])$')
			type5 = re.compile(r'^([1-9][0-9][0-9][0-9])年(0?[1-9]|1[0-2])月(0?[1-9]|1[0-9]|2[0-9]|3[0-1])日$')
			type6 = re.compile(r'^([1-9][0-9][0-9][0-9])-(0?[1-9]|1[0-2])-(0?[1-9]|1[0-9]|2[0-9]|3[0-1]) (0?[0-9]|1[0-9]|2[0-3]):(0?[0-9]|[1-5][0-9]):(0?[0-9]|[1-5][0-9])$')
			type7 = re.compile(r'^([1-9][0-9][0-9][0-9])/(0?[1-9]|1[0-2])/(0?[1-9]|1[0-9]|2[0-9]|3[0-1]) (0?[0-9]|1[0-9]|2[0-3]):(0?[0-9]|[1-5][0-9]):(0?[0-9]|[1-5][0-9])$')
			type8 = re.compile(r'^([1-9][0-9][0-9][0-9])年(0?[1-9]|1[0-2])月(0?[1-9]|1[0-9]|2[0-9]|3[0-1]) (0?[0-9]|1[0-9]|2[0-3]):(0?[0-9]|[1-5][0-9]):(0?[0-9]|[1-5][0-9])$')
			type9 = re.compile(r'^([1-9][0-9][0-9][0-9])年(0?[1-9]|1[0-2])月(0?[1-9]|1[0-9]|2[0-9]|3[0-1])日 (0?[0-9]|1[0-9]|2[0-3]):(0?[0-9]|[1-5][0-9]):(0?[0-9]|[1-5][0-9])$')

			if type1.match(strs):
				ltime   = time.localtime(int(strs))
				content = time.strftime("%Y-%m-%d %H:%M:%S", ltime)
			elif type2.match(strs):
				timeArray = time.strptime(strs, "%Y-%m-%d")
				content   = str(int(time.mktime(timeArray)))
			elif type3.match(strs):
				timeArray = time.strptime(strs, "%Y/%m/%d")
				content   = str(int(time.mktime(timeArray)))
			elif type4.match(strs):
				timeArray = time.strptime(strs, "%Y年%m月%d")
				content   = str(int(time.mktime(timeArray)))
			elif type5.match(strs):
				timeArray = time.strptime(strs, "%Y年%m月%d日")
				content   = str(int(time.mktime(timeArray)))
			elif type6.match(strs):
				timeArray = time.strptime(strs, "%Y-%m-%d %H:%M:%S")
				content   = str(int(time.mktime(timeArray)))
			elif type7.match(strs):
				timeArray = time.strptime(strs, "%Y/%m/%d %H:%M:%S")
				content   = str(int(time.mktime(timeArray)))
			elif type8.match(strs):
				timeArray = time.strptime(strs, "%Y年%m月%d %H:%M:%S")
				content   = str(int(time.mktime(timeArray)))
			elif type9.match(strs):
				timeArray = time.strptime(strs, "%Y年%m月%d日 %H:%M:%S")
				content   = str(int(time.mktime(timeArray)))
			else:
				break

			self.view.run_command('cut')
			self.view.insert(edit, s.begin(), content)

class MagicNewTimeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for s in self.view.sel():
			content = str(int(time.time()))
			if not s.empty() or s.size() > 1:
				self.view.run_command('cut')

			self.view.insert(edit, s.begin(), content)