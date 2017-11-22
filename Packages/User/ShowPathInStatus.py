# -*- coding: utf-8 -*-
'''
Plugin for Sublime Text to show the path of the current
file in the status bar. The path start from the project
directory or user home directory.

You can also copy this path to the clipboard with the
copy_path command
'''

import sublime
import sublime_plugin
from os.path import expanduser

__author__ = "Francisco Jesús Jiménez Cabrera (jkfran)"
__email__ = "jkfran@gmail.com"


class ShowPathInStatus(sublime_plugin.EventListener):
    def get_short_path(self, view):
        path = view.file_name()

        if path:
            if view.window().project_data():
                for folder in view.window().project_data()['folders']:
                    project_path = folder.get('path')
                    if path.startswith(project_path):
                        path = path[len(project_path):].lstrip('/')
                        break

            home_path = expanduser("~")
            if path.startswith(home_path):
                path = path[len(home_path):].lstrip('/')

        return path

    def on_activated(self, view):
        view.set_status('_filename', self.get_short_path(view))


class CopyPathCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.set_clipboard(self.view.get_status("_filename"))
