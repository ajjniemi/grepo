import os
import sys

def main():
	if len(sys.argv) != 2:
		print "Use: Python grepo.py /your/path/to/repo"
		sys.exit(1)
	else:
		repo = sys.argv[1]
	
		os.chdir('%s' % repo)
		os.system('git init')
main()
