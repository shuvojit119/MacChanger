#!/usr/bin/python

import subprocess,optparse,re

def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option('-i','--interface ',dest='interface',help=' interface to change MAC address. ')
    parser.add_option('-m','--mac ',dest='new_mac',help=' new MAC address. ')
    (options,arguments) =  parser.parse_args()
    if not options.interface:
        parser.error('[e] Please specify an interface, use -h or --help for more info.')
    elif not options.new_mac:
        parser.error('[e] Please specify an mac, use -h or --help for more info.')
    return options



def mac_changer(interface,new_mac):

    print('[+] Changing MAC address for '+interface+" to "+new_mac)
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])



def get_current_mac(interface):
    ifconfig_result=subprocess.check_output(['ifconfig',interface])

    mac_s_result=re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)
    if mac_s_result:

        return  mac_s_result.group(0)
    else:
        print('[0] could not read mac address')

options = get_arguments()

current_mac=get_current_mac(options.interface)
print('Current Mac = '+str(current_mac))

mac_changer(options.interface,options.new_mac)

current_mac=get_current_mac(options.interface)

if current_mac == options.new_mac:
    print("MAC Changed [OK]. "+ current_mac)

else:
    print('MAC address did not  changed [0].')

