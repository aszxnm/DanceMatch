import os
import numpy as np

exp_len = 359
frame = 128

def main(audio_path, video_path):
    audio_list = os.listdir(audio_path)
    audioexp = np.zeros((1,frame,exp_len))
    for audio in audio_list:
        print(audio)
        audio_file = os.path.join(audio_path, audio)
        video_file = os.path.join(video_path, audio[:-4], 'data', audio[:-4]+'.npy')
        data_video = np.load(video_file, allow_pickle=True)
        data_audio = np.load(audio_file)
        tmp = np.zeros((1,exp_len))
        flag = True
        num = 0
        for i in range(len(data_video)):
            if(data_video[i][0] >= len(data_audio)): break
            audiof = data_audio[data_video[i][0]].reshape(1, -1)
            expose = np.concatenate((audiof, data_video[i][1]), axis=1)
            expose = np.concatenate((expose, data_video[i][2]), axis=1)
            if flag:
                tmp = np.concatenate((tmp, expose), axis=0)
                flag = False
                num += 1
                continue
            if data_video[i][0] - data_video[i-1][0] == 1:
                tmp = np.concatenate((tmp, expose), axis=0)
                num += 1
            else:
                tmp = np.zeros((1,exp_len))
                tmp = np.concatenate((tmp, expose), axis=0)
                num = 1
                
            if num % frame == 0:
                tmp = tmp[1:, :].reshape(1, frame, exp_len)
                audioexp = np.concatenate((audioexp, tmp), axis=0)
                tmp = np.zeros((1,exp_len))
                num = 0
                flag = True
        print(audioexp.shape)
    np.save('train.npy', audioexp[1:, :, :])

if __name__ == '__main__':
    audio_path = './audio_result'
    video_path = './result'
    main(audio_path, video_path)
