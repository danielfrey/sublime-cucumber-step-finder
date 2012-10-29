# -*- coding: utf-8 -*-
import sublime, sublime_plugin
import os
import re
import codecs

class CucumberStepFinderCommand(sublime_plugin.WindowCommand):
  def __init__(self, window):
    sublime_plugin.WindowCommand.__init__(self, window)
    self.recent_files = []
    self.enabled      = True
    self.load_settings()

  def load_settings(self):
    self.settings = sublime.load_settings("CucumberStepFinder.sublime-settings")
    self.features_path = self.settings.get('cucumber_features_path')  # Default is "features"
    self.step_pattern = self.settings.get('cucumber_step_pattern')    # Default is '.*_steps.*\.rb'

  def run(self, file_name=None):
    self.find_all_steps()

  def find_all_steps(self):
    pattern = re.compile(r'((.*)(\/\^.*))\$\/')
    self.steps = []
    folders = self.window.folders()
    for folder in folders:
      for path in os.listdir(folder):
        full_path = os.path.join(folder, path)
        if path == self.features_path:
          self.step_files = []
          for root, dirs, files in os.walk(full_path):
            for f_name in files:
              if re.match(self.step_pattern, f_name):
                self.step_files.append((f_name, os.path.join(root, f_name)))
                step_file_path = os.path.join(root, f_name)
                with codecs.open(step_file_path, encoding='utf-8') as f:
                  index = 0
                  for line in f:
                    match = re.match(pattern, line)
                    if match:
                      self.steps.append((match.group(), index, step_file_path))
                    index += 1
                      # print match.group()

    steps_only = [x[0] for x in self.steps]
    self.window.show_quick_panel(steps_only, self.step_found)


  def step_found(self, index):
    if index >= 0:
      # print self.steps[index][2], self.steps[index][1]
      file_path = self.steps[index][2]
      view = self.window.open_file(file_path)

      self.active_ref = (view, self.steps[index][1])
      # self.highlight_step(view, self.steps[index][1])
      self.mark_step()


  def mark_step(self):

    view = self.window.active_view()

    if view.is_loading():
      sublime.set_timeout(self.mark_step, 50)
    else:
      # if view == self.active_ref[0]:
      view.run_command("goto_line", {"line": self.active_ref[1]+1} )



