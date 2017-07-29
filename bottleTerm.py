import bottles
import argparse
import sys

class customParser(argparse.ArgumentParser):
    def error(self, message):
                sys.stderr.write('error: %s' % message + ', running with default behavior instead\n')
                bottles.start()


parser = customParser()
parser.add_argument("bottles", help="Number of bottles to count down from", type=int)
parser.add_argument("delay", help="Delay between lines printed", type=int)
args = parser.parse_args()

bottles.singMeAGoddamnSong(args.bottles, args.delay)
