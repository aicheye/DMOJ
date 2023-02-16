S = int(input())
W = int(input())
if 20 <= S <= 23 :
    if 6 <= W <= 9 :
        if 8 <= (24 - S) + W <= 10 :
            print("Healthy")
        else :
            print("Unhealthy")
    else :
        print("Unhealthy")
else :
    print("Unhealthy")
