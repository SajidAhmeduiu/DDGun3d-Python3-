#/usr/bin/env python
import os, sys, time, threading
from commands import getstatusoutput
global prog_path


class progress_bar_loading(threading.Thread):

	def run(self):
		global stop, kill
		sys.stdout.flush()
		i = 0
		while stop != True:
			if (i%4) == 0: 
				sys.stdout.write('\b/')
			elif (i%4) == 1:
				sys.stdout.write('\b-')
			elif (i%4) == 2:
				sys.stdout.write('\b\\')
			elif (i%4) == 3:
				sys.stdout.write('\b|')
			sys.stdout.flush()
			time.sleep(0.2)
			i+=1
		if kill == True:
			print '\b Abort!',
			sys.exit()
		else:
			print '\b ',
		
			

def task_1():
	cmd='cd '+prog_dir+'/utils/;'
	cmd=cmd+'git clone https://github.com/soedinglab/hh-suite.git;'
	cmd=cmd+'mkdir -p hh-suite/build && cd hh-suite/build;'
	cmd=cmd+'cmake -DCMAKE_INSTALL_PREFIX=.. ..;'
	cmd=cmd+'make -j 4 && make install'
	out=getstatusoutput(cmd)
	if out[0]!=0:
		print >>sys.stderr,'ERROR: hhblits not installed\n',out[1]
		os._exit(1)
		#sys.exit(1)
	cmd='cd '+prog_dir+'/utils/hh-suite/bin;pwd;./hhblits -h'
	out=getstatusoutput(cmd)
	if out[0]!=0:
		print '\b '
		print >>sys.stderr,'ERROR: Incorrect hhblits installation\n',out[1]
		os._exit(2)
		#sys.exit(2)
	print '\b   done!'
	return


def task_2():
	www_uc30='http://wwwuser.gwdg.de/~compbiol/uniclust/2018_08/uniclust30_2018_08_hhsuite.tar.gz'
	file_uc30='uniclust30_2018_08_hhsuite.tar.gz'
	cmd='cd '+prog_dir+'/data/;'
	cmd=cmd+'wget -q '+www_uc30+';'
	cmd=cmd+'ls '+file_uc30
	out=getstatusoutput(cmd)
	if out[0]!=0:
		print >>sys.stderr,'ERROR: uniclust30_2018_08 not downloaded\n',out[1]
		os._exit(3)
		#sys.exit(3)
	print '\b   done!'
	return


def task_3():
	file_uc30='uniclust30_2018_08_hhsuite.tar.gz'
	cmd='cd '+prog_dir+'/data/;'
	cmd=cmd+'tar -xzvf '+file_uc30
	out=getstatusoutput(cmd)
	if out[0]!=0:
		print >>sys.stderr,'ERROR: untar uniclust30_2018_08 not completed\n',out[1]
		os._exit(4)
		#sys.exit(4)
	print '\b   done!'
	return



def main():
	global prog_dir, stop, kill
	prog_dir = os.path.dirname(os.path.abspath(__file__))
	kill = False
	stop = False
	p = progress_bar_loading()
	p.start()
	try:
		print >> sys.stderr,'1) Install hhblits'	
    		task_1()
		print >> sys.stderr,'2) Download uniclust30_2018_08 (25Gb)'
    		task_2()
		print >> sys.stderr,'3) Untar uniclust30_2018_08 (25Gb)'
		task_3()
		time.sleep(1)
		stop=True
	except KeyboardInterrupt or EOFError:
		kill = True
		stop = True
	


if __name__ == '__main__':
	main()
	