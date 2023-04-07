import os


# 遍历文件
def get_file(file_path, file_format):
    """

    :param file_path: 需要遍历文件的文件夹
    :param file_format: 需要遍历文件的类型
    :return: 遍历后的文件列表
    """
    get = []  # 函数返回结果
    for filenames in os.listdir(file_path):  # 遍历文件
        if filenames.split('.')[1] == file_format:
            get.append(os.path.join(file_path, filenames))
    return get


def ffmpeg_transition(file_path, directory, target_format):
    """

    :param file_path: 原始音频的文件路径
    :param directory: 转换后音频文件的保存目录
    :param target_format: 需要转换后的音频格式
    :return: 无
    """
    file_name = os.path.split(file_path)[1].split('.')[0]  # 路径拆分，文件名和文件格式拆分，获取文件名
    # ffmpeg命令,w4a转换wav
    command = f'ffmpeg -i "{file_path}" -ac 1 -ar 160000 "{os.path.join(directory, file_name)}.{target_format}"'
    os.system(command)  # 执行命令, 成功返回0，失败返回1


file_format = "m4a"  # 需要转换的文件格式
target_format = 'wav'  # 目标格式 音频转换后的格式
audio_path = ".\\audio"  # 需要转换的音频文件路径
directory = ".\\audio_wav"  # 转换后的文件保存目录


# 如果没有这个目录则创建目录
if not os.path.exists(directory):  
    os.mkdir(directory)

# 返回所有音频文件
file_list = get_file(audio_path, file_format)

# 对音频文件进行格式转换
for file in file_list:
    ffmpeg_transition(file, directory, target_format)
