import os
import glob
import sys

try:
    path = sys.argv[1]
except IndexError:
    path = ""

overwrite = "-w" in sys.argv

ffmpeg_cmd = """ffmpeg -i "%s"  -c:v libx264 -crf 23  -q:a 100 "%s" """

from_ext = '.wmv'
to_ext = '.mp4'

input_video_files = glob.glob(os.path.join(path, "*" + from_ext))
for video in input_video_files:
    print("Processing %s" % (video,))
    output_name = os.path.splitext(video)[0] + to_ext
    if os.path.exists(output_name) and not overwrite:
        print("Output file exists. Skipping. (pass -w to overwrite)")
        continue
    cmd = ffmpeg_cmd % (video, output_name)
    os.system(cmd)
