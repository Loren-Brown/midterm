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
import os, time, subprocess, clr

import MissionPlanner
clr.AddReference("MissionPlanner.Utilities")


print 'Start Script'
for chan in range(1,9):
	Script.SendRC(chan,1500,False)
	Script.SendRC(3,Script.GetParam('RC3_MIN'),True)
	Script.Sleep(1000)	
print 'Setup Done'

user = 'ground'
while 1:
	#user = raw_input('>>')
	#user = 'ground'
	if user == 'ping':
		start_time = int(round(time.time() * 1000))
		m = cs.mode
		end_time = int(round(time.time() * 1000))
		print (end_time - start_time)
		
	elif user == 'ground' :
		#user = raw_input('Min altitude in meters: ')
		#user = 3
		user_alt = 1.0 #float(user)
		while 1 :
			print cs.alt
			if cs.alt > user_alt:
				Script.Sleep(50) #ms
			else :
				print 'TOO LOW!'
				
				print 'Seting flight mode to LOITER'
				#Script.ChangeMode("LOITER")
				MAV.setMode("LOITER")
				Script.Sleep(1000) #ms
				print 'Checking flight mode'
				print cs.mode
				
				print 'Wait for drone (2 sec)'
				Script.Sleep(3000) #ms
				
				print 'Setting New Waypoint'
				wp = MissionPlanner.Utilities.Locationwp()
				print 'Moving up 1m'
				new_alt = cs.alt + 1
				MissionPlanner.Utilities.Locationwp.lat.SetValue(wp,cs.lat)
				MissionPlanner.Utilities.Locationwp.lng.SetValue(wp,cs.lng)
				MissionPlanner.Utilities.Locationwp.alt.SetValue(wp,new_alt)
				print 'Waypoint Set'
				MAV.setGuidedModeWP(wp)
				
				print 'Waiting on waypoint'
				while(cs.alt < new_alt) :
					print cs.alt
					Script.Sleep(500) #ms
				
				print 'Seting flight mode to STABILIZE'
				#Script.ChangeMode("STABILIZE")
				MAV.setMode("STABILIZE")
				Script.Sleep(1000) #ms
				
				print 'Checking flight mode'
				print cs.mode
				
				print 'Done'
				print 'Disabling ground avoidance'
				user = ''
				break

	else:
		print 'Ending Script'
		break
	
	