from moviepy.editor import VideoFileClip, concatenate_videoclips

import sys

def main():
    clips = sys.argv[1:]
    clips.sort()
    
    file_name = str(clips[0].split('/')[-1]).split('.MP4')[0]
    
    video_clips = []
    for clip in clips:
        video_clips.append(VideoFileClip(clip))
    
    final_clip = concatenate_videoclips(video_clips)
    final_clip.write_videofile('%s_complete.mp4' % file_name, fps=24, codec='libx264', threads=4)

if __name__ == '__main__':
    main()
