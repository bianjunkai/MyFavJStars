#!/usr/bin/expect -f
set user root
set port 26716
set host 97.64.19.253
set password mkUaT5aTYSVd
set timeout -1
 
spawn ssh -p $port $user@$host
expect "*assword:*"
send "$password\r"
interact
expect eof
