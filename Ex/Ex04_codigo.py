def capturaSinalSecreto(ar):
    A=open; s=len
    import requests, numpy as np,scipy as sp
    from scipy.io import wavfile
    from scipy import signal
    X=requests.get('https://github.com/ifmg-betim/2023.2_AUT.040_ProcSin/blob/main/Ex/Ex04_arquivo.w123?raw=true')
    A("Ex04_arquivo.w123","wb").write(X.content)
    fs,v=wavfile.read('Ex04_arquivo.w123')
    v=v[:,0]; L=np.arange(s(v))/fs; np.random.seed(ar*123-5); c1,c2,c3=np.random.randint(0,11,3);
    t1, t2, t3 = np.arange(c1*48000,c1*48000+45000), np.arange(c2*48000,c2*48000+45000), np.arange(c3*48000,c3*48000+45000)
    T=np.hstack((v[t1],v[t2],v[t3])); m=np.arange(s(T))/fs; T=T+np.random.normal(0,1e3,s(T))
    c4, r1 = np.random.randint(5e3,20e3), np.random.normal(0,3e3,s(T))
    d2,n1=signal.iirdesign([(c4-2000)*2/fs,(c4+2000)*2/fs],[(c4-800)*2/fs,(c4+800)*2/fs],1,40)
    K=T*np.sin(2*np.pi*c4*m+10*np.random.rand())+signal.filtfilt(d2,n1,r1)
    return K,fs