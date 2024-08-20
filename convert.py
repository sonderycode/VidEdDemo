import os
# from moviepy.editor import VideoFileClip
import imageio

def convert_mp4_to_gif(input_folder, output_folder):
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)
    
    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4"):
            mp4_path = os.path.join(input_folder, filename)
            gif_name = os.path.splitext(filename)[0] + ".gif"
            gif_path = os.path.join(output_folder, gif_name)
            
            # 加载视频文件并转换为 GIF
            clip = VideoFileClip(mp4_path)
            clip.write_gif(gif_path)
            print(f"Converted {filename} to {gif_name}")

def set_gif_loop(input_dir, output_dir, loop_count):
    # 如果输出目录不存在，创建它
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 遍历输入目录中的所有文件
    for filename in os.listdir(input_dir):
        if filename.endswith('.gif'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            # 读取 GIF 文件
            gif = imageio.mimread(input_path)

            # 重新保存 GIF 文件，设置循环次数
            imageio.mimsave(output_path, gif, loop=loop_count)
            print(f"Processed {filename}, saved to {output_path}")



# 输入文件夹和输出文件夹路径
input_folder = "Video_edit/video"
output_folder = "Video_edit/video_ori"

# convert_mp4_to_gif(input_folder, output_folder)


input_folder = "Video_edit/Tune-A-Video"
output_folder = "Video_edit/Tune-A-Video_loop"
loop_count = 500  # 设置循环次数，0 表示无限循环

set_gif_loop(input_folder, output_folder, loop_count)
