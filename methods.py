import math
import file_import as fi
import dataclass as cd

#ここでは、同じフォルダに全てのファイルがある想定。そのフォルダ内のファイルを利用
def trans_cor(LogSheet, ICdata, qr=(0.025, 1.8), Dpath='', Spath=''):
    Log_df=fi.read_Log(LogSheet)
    IC_df=fi.read_IC(ICdata)
    qr=qr
    
    def method1(file):
        data=fi.read_chi(Dpath+file+'.chi')
        IC2=IC_df.at[file, 'IC2']
        data['I_t']=data['I']/IC2

        return data
    
    for i in Log_df.index:
        datafile=Log_df.at[i, 'filename']
        solname=Log_df.at[i, 'solvent_name']
        cons=Log_df.at[i, 'correc_cons']

        if solname=='skip':
            result=method1(datafile)
        else:
            solfile=Log_df.at[solname, 'filename']
            result=method1(datafile)
            result['I_t_subsol']=result['I_t']-method1(solfile)['I_t']
            result['I_abs']=result['I_t_subsol']*cons
        
        result=result.query('@qr[0]<q<@qr[1]')
        result.to_csv(Spath+i+'.csv', index=None)


