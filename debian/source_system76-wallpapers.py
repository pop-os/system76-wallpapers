"""
Apport package hook for system76-wallpapers (requires Apport 2.5 or newer).

Copyright (C) 2014 System76, Inc.
"""

def add_info(report):
    report['CrashDB'] = "{'impl': 'launchpad', 'project': 'system76-wallpapers'}"

