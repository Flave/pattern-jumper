import sublime, sublime_plugin

class JumperCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Jumpto Section:", "", None, self.on_change, None)
		pass

	def on_change(self, text):
		try:
			if self.window.active_view():
				self.window.active_view().run_command("jump_to_section", {"key": text, "pattern": "/// "})
		except ValueError:
			pass


class JumpToSectionCommand(sublime_plugin.TextCommand):
	def run(self, edit, key, pattern):
		region = self.view.find(pattern + key, 0, sublime.IGNORECASE)
		if region:
			self.view.show(region.begin())