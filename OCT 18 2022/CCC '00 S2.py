def streamSplit(streams, toSplit, flowL) :
    streamL = streams[toSplit - 1] * flowL / 100
    streamR = streams[toSplit - 1] - streamL
    streams.insert(toSplit - 1, streamR)
    streams.insert(toSplit - 1, streamL)
    streams.pop(toSplit + 1)
    return streams


def streamJoin(streams, toJoinL) :
    streams[toJoinL - 1] = streams[toJoinL - 1] + streams[toJoinL]
    streams.pop(toJoinL)
    return streams


if __name__ == '__main__' :
    inStreams = []
    for i in range(int(input())) :
        inStreams.append(int(input()))
    stillFalling = True
    while stillFalling :
        command = int(input())
        if int(command) == 99 :
            inToSplit = int(input())
            inFlowL = int(input())
            streamSplit(inStreams, inToSplit, inFlowL)
        elif int(command) == 88 :
            inToJoinL = int(input())
            streamJoin(inStreams, inToJoinL)
        else :
            stillFalling = False
    for i in range(len(inStreams)) :
        print(round(inStreams[i]), end=" ")
