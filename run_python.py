#/usr/bin/env python2

from subprocess import call
from optparse import OptionParser
import sys
import os
from gnuradio import gr, gru, eng_notation
from gnuradio.eng_option import eng_option
import shutil

def get_options():
	usage="%prog: [options] output_filename"
	parser = OptionParser(option_class=eng_option, usage=usage)
	parser.add_option("-f", "--freq", type="eng_float", default=2.4e9,
					  help="USRP center frequency in Hz")
	parser.add_option("-g", "--gain", type="eng_float", default=5,
					  help="USRP Gain in dB")
	parser.add_option("-t", "--time", type="eng_float", default=3,
					  help="Duration of scan")
	parser.add_option("-s", "--samp", type="eng_float", default=200e6,
					  help="Sampling rate (in Samp/s)")
	parser.add_option("-n", "--nfile", type="eng_float", default=1,
					  help="Number of consecutive experiments")


	(options, args) = parser.parse_args()
	return (options)

if __name__ == '__main__':
	(options) = get_options()
	duration = options.time
	files = int(options.nfile)
	samp = options.samp
	no_samples = duration * samp
	gain = options.gain
	freq = options.freq

	call(["mkdir", "ramdisk"])
	call(["mkdir", "IQ"])
	call(["sudo", "mount", "-t", "tmpfs", "-o", "size=14000m", "tmpfs", "ramdisk"])
	for i in range(files):
		call(["python", "uhd_rx_cfile.py", "-f", str(freq), "-r", str(samp), "-N", str(no_samples), "-m", "-g", str(gain), "-s"])
		#call(["mv", os.getcwd()+ "/ramdisk/*", os.getcwd() + "/IQ"])
		files = os.listdir("ramdisk/")
		for f in files:
			shutil.move("ramdisk/"+f, "IQ/")

	call(["sudo", "umount", os.getcwd() + "/ramdisk"])
	call(["rm", "-rf", os.getcwd() + "/ramdisk"])
