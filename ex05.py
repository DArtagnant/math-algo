N= 4529
def hms(N):
    h=N//3600
    N=N%3600
    m=N//60
    s=N//60
    return h,m,s

print("heures : {}, minutes : {}, secondes : {}".format(*hms(N)))
