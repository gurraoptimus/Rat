import subprocess
import os

class AndroidCTL:
    def __init__(self, adb_path='adb'):
        self.adb_path = adb_path

    def run_command(self, command):
        result = subprocess.run([self.adb_path] + command.split(), capture_output=True, text=True)
        return result.stdout.strip()

    def list_devices(self):
        return self.run_command('devices')

    def install_app(self, apk_path):
        return self.run_command(f'install {apk_path}')

    def uninstall_app(self, package_name):
        return self.run_command(f'uninstall {package_name}')

    def start_activity(self, package_name, activity_name):
        return self.run_command(f'shell am start -n {package_name}/{activity_name}')

    def stop_app(self, package_name):
        return self.run_command(f'shell am force-stop {package_name}')

    def get_logcat(self):
        return self.run_command('logcat -d')

if __name__ == "__main__":
    ctl = AndroidCTL()
    print("Connected devices:")
    print(ctl.list_devices())