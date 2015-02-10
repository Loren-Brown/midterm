# cs.???? = currentstate, any variable on the status tab in the planner can be used.
# Script = options are
# Script.Sleep(ms)
# Script.ChangeParam(name,value)
# Script.GetParam(name)
# Script.ChangeMode(mode) - same as displayed in mode setup screen 'AUTO'
# Script.WaitFor(string,timeout)
# Script.SendRC(channel,pwm,sendnow)
#
import sys
sys.path.append(r"c:\Python27\Lib\site-packages")
sys.path.append(r"c:\Python27\Lib")
#sys.path.append(r"c:\Python27\Lib\lib-tk")
#sys.path.append("c:\Python27\libs")
#sys.path.append(r"c:\Python27\DLLs")
#sys.path.append(r"c:\Python27")

import os, time, subprocess


print 'Start Script'
for chan in range(1,9):
	Script.SendRC(chan,1500,False)
	Script.SendRC(3,Script.GetParam('RC3_MIN'),True)
	#Script.Sleep(1000)	
print 'Setup Done'

print 'Ping'
start_time = int(round(time.time() * 1000))
m = cs.mode
end_time = int(round(time.time() * 1000))
print (end_time - start_time), 
print 'ms'
print m
print cs.armed