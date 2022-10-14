import matplotlib.pyplot as plt
import numpy as np

class SAXSdata:
    def __init__(self, df):
        self.name=self
        self.q=df['q']
        self.I=df['I']
        self.df=df

    def profile(self, color='red', scale='loglog', label='untitled'):
        plt.plot(self.q, self.I, c=color, label=label)
        plt.xscale('log')
        plt.yscale('log')
        plt.xlabel('$q$ (nm$^{-1}$)')
        plt.ylabel('I($q$) (cm$^{-1}$)')
        plt.grid(ls='dotted', c='gray', lw=1)

    """def gunierplot(self, Rq=1):

        i=10
        df=self.df[:i]

        def fitting(df):
            q2=df['q']**2
            lnIq=np.log(df['I_t_subsol'])
            slope, intercept=np.polyfit(q2, lnIq, 1)
            Rg=(-3*slope)**0.5
            return slope, intercept, Rg

        while fitting(df)[2]*(df['q'].tail(1).item()**2)<1:
            i+=1
        
        fitting(df)
            
        x=np.linspace(0, max(df['q'].tail(1).item())*1.1, 1000)

        plt.plot(fitting(df)[0], fitting(df)[1], 'o', lw=0)
        plt.plot(x,fitting(df)[0]*x+fitting(df)[1])

        plt.xlabel('$q^2$')
        plt.ylabel('ln(I($q$))')"""


