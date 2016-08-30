
import datetime
import subprocess 


class fileBackerUpper(object):
    def __init__(self):

    def _execute_bash_cmd(self, cmd):
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        return proc.communicate()[0]

    def git_commit_changes(self):
        # self._execute_bash_cmd('cron command goes here')
        self._execute_bash_cmd('cd C:\Users\Tom\Desktop\file_backup')
        self._execute_bash_cmd('git add .')
        self._execute_bash_cmd('git commit -a -m "' + str(datetime.datetime.now()) + '"')
        self._execute_bash_cmd('git push origin master')

if __name__ == '__main__':
    fileBackerUpper().git_commit_changes()
