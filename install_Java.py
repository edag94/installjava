import requests
import os
import subprocess
import shutil

print("Creating temp dir for Java installer")
home = os.path.expanduser("~")
temp_dir_name = "tmp"
temp_path = os.path.join(home,temp_dir_name)
if not os.path.exists(temp_path):
    os.mkdir(temp_path)

config_contents = '''INSTALL_SILENT=Enable
AUTO_UPDATE=Enable
SPONSORS=Disable
REMOVEOUTOFDATEJRES=1
'''

print("Writing Java installation config file")
config_file_path = os.path.join(temp_path,"jreinstall.cfg")
with open(config_file_path, "w+") as config_file:
    config_file.write(config_contents)

print("Downloading Java installer")

source = "https://javadl.oracle.com/webapps/download/AutoDL?BundleId=239855_230deb18db3e4014bb8e3e8324f81b43"
destination = os.path.join(temp_path,"jreInstall.exe")

r = requests.get(source, stream = True) 
# download started 
with open(destination, 'wb') as f: 
    for chunk in r.iter_content(chunk_size = 1024*1024): 
        if chunk: 
            f.write(chunk)


print("Running installer")
cmd = destination + " " + "INSTALLCFG=" + config_file_path
subprocess.call(cmd, shell=True)
print("Installing Java. This make take up to 3 minutes...")
print("Success!")

print("Deleting installer")
shutil.rmtree(temp_path)




