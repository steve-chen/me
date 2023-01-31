#!/usr/bin/env python3

import os, os.path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("video_file")
args = parser.parse_args()

video_file = args.video_file
filename, ext = os.path.splitext(video_file)

cmd_first_pass = f"ffmpeg -i {args.video_file} -vf vidstabdetect -f null -" 
cmd_second_pass = f"ffmpeg -i {args.video_file} -vf vidstabtransform {filename}_stabilized.mp4" 

os.system(cmd_first_pass)
os.system(cmd_second_pass)

