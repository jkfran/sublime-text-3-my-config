# -*- coding: utf-8 -*-
'''
Plugin for Sublime Text to show the path of the current
file in the status bar. The path start from the project
directory or user home directory.
'''

import sublime_plugin
from os.path import expanduser

__author__ = "Francisco Jesús Jiménez Cabrera (jkfran)"
__email__ = "jkfran@gmail.com"


class ShowPathInStatus(sublime_plugin.EventListener):
    def on_activated_async(self, view):
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

            view.set_status('_filename', path)
