import os
import fnmatch


# get all files
def dir_list(path, allfiles):
    """
    :param path: 文件的路径
    :param allfiles: 存放文件地址的列表
    :return: 返回所有的文件列表
    """
    filelists = os.listdir(path)
    for filename in filelists:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dir_list(filepath, allfiles)
        elif fnmatch.fnmatch(filepath, '*.mp4'):  # 判断文件格式
            allfiles.append(filepath)

    return allfiles


# 分辨率的转换
def RunScript(fileList):
    print('*' * 15 + 'Start to run:')
    """ffmpeg -i 3.mp4 -vn -y -acodec copy 3.aac
       ffmpeg -i 2018.mp4 -codec copy -bsf: h264_mp4toannexb -f h264 tmp.264
       ffmpeg -i killer.mp4 -an -vcodec copy out.h264
    """

    # 分离音频的执行命令前部分    {}{}分别为原始视频  与输出后保存的路径名
    code_yin = 'ffmpeg -i {} -f wav -ar 16000 {}'

    # code_Mid = ' -vf scale=480:848 {} -hide_banner'
    for filename in fileList:
        # 视频名称
        #print(filename)
        input_name = filename.split('.')[1].split('/')[-1]
        # print(input_name)

        out_yin_name = input_name + '.wav'
        # h264视频流的输路径
        out_yinpin_path = os.path.join(New_Save_path, out_yin_name)
 
        # 最终执行提取音频的指令
        code_finish_yin = code_yin.format(filename, out_yinpin_path)

        # print('*'* 20 + finish_code)
        os.system(code_finish_yin)

    print('End #################')


if __name__ == '__main__':
    global fileDir
    fileDir = "./video"
    global New_Save_path
    New_Save_path = "./audio"
    allfile = []
    dir_list(fileDir, allfile)
    RunScript(allfile)
