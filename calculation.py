import numpy as np
class Calculate:
 
    def __init__(self, S, E, I, R, b, y, sigma, v, u, p, t, h):
        self.S = S
        self.E = E
        self.I = I
        self.R = R
        self.u = u
        self.p = p
        self.b = b
        self.v = v
        self.sigma = sigma
        self.y = y
        self.N = S + E + I + R
        self.h = h
        self.t = t
    

    def findAll(self):
        Si = self.S
        Ei = self.E
        Ii = self.I
        Ri = self.R
        arrayT = np.array([])
        arrayS = np.array([])
        arrayE = np.array([])
        arrayI = np.array([])
        arrayR = np.array([])

        i = 0
        while i<self.t:
           arrayT = np.append(arrayT,i)

           k1,k2,k3,k4 = self.findKforS(Si, Ri, Ii)
           Si+=(self.h/6)*(k1+2*k2+2*k3+k4)
           arrayS = np.append(arrayS,Si)

           k1,k2,k3,k4 = self.findKforE(Ei, Ii, Si)
           Ei+=(self.h/6)*(k1+2*k2+2*k3+k4)
           arrayE = np.append(arrayE,Ei)

           k1,k2,k3,k4 = self.findKforI(Ii, Ei)
           Ii+=(self.h/6)*(k1+2*k2+2*k3+k4)
           arrayI = np.append(arrayI,Ii)

           k1,k2,k3,k4 = self.findKforR(Ri, Ii, Si)
           Ri+=(self.h/6)*(k1+2*k2+2*k3+k4)
           arrayR = np.append(arrayR,Ri)

           self.N = Si + Ei + Ii+ Ri

           i+=self.h

        return [arrayS, arrayE, arrayI, arrayR, arrayT]




    def findKforS(self, S, R, I):
         k1 = self.diffS(S, R, I)
         k2 = self.diffS(S+(k1*self.h)/2, R+self.h/2, I + self.h/2)
         k3 = self.diffS(S+(k2*self.h)/2, R+self.h/2, I + self.h/2)
         k4 = self.diffS(S+k3*self.h, R+self.h, I + self.h)
         return k1,k2,k3,k4

    def findKforE(self, E, I, S):
         k1 = self.diffE(E, I, S)
         k2 = self.diffE(E+(k1*self.h)/2, I+self.h/2, S + self.h/2)
         k3 = self.diffE(E+(k2*self.h)/2, I+self.h/2, S + self.h/2)
         k4 = self.diffE(E+k3*self.h, I+self.h, S + self.h)
         return k1,k2,k3,k4

    def findKforI(self, I, E):
         k1 = self.diffI(I, E)
         k2 = self.diffI(I+(k1*self.h)/2, E+self.h/2)
         k3 = self.diffI(I+(k2*self.h)/2, E+self.h/2)
         k4 = self.diffI(I+k3*self.h, E+self.h)
         return k1,k2,k3,k4

    def findKforR(self, R, I, S):
         k1 = self.diffR(R, I, S)
         k2 = self.diffR(R+(k1*self.h)/2, I+self.h/2, S + self.h/2)
         k3 = self.diffR(R+(k2*self.h)/2, I+self.h/2, S + self.h/2)
         k4 = self.diffR(R+k3*self.h, I+self.h, S + self.h)
         return k1,k2,k3,k4




    def diffS(self, S, R, I):
       # return self.u*(self.N-S) + self.p*R - self.b*(S*I)/self.N - self.v*S
       return self.u*self.N + self.p*R - self.b*(S*I)/self.N - self.v*S
    def diffE(self, E, I, S):
       # return (self.b*S*I)/self.N - (self.u+self.sigma)*E 
        return (self.b*S*I)/self.N - (self.v+self.sigma)*E 
    def diffI(self, I, E):
      #  return self.sigma*E - (self.u + self.y)*I
        return self.sigma*E - (self.v + self.y)*I
    def diffR(self, R, I, S):
      #  return self.y*I - self.u*R + self.v*S - self.p*R
        return self.y*I - self.v*R - self.p*R
