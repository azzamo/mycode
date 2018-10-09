#!/usr/bin/env python3

import shutil
import os

os.chdir('/home/student/mycode/')

shutil.copy('5g_research/sdn_network.txt','/home/student/mycode/sdn_network.txt_copy')

shutil.copytree('5g_research/','5g_research_bakup')

# The following line will create the directory if it does not exist already
