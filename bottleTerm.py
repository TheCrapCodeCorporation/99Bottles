import bottles
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("bottles", help="Number of bottles to count down from", type=int)
parser.add_argument("delay", help="Delay between lines printed", type=int)
args = parser.parse_args()

bottles.singMeAGoddamnSong(args.bottles, args.delay)
