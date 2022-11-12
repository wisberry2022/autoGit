import os
import sys


class AGMachine:
    def __init__(self):
        self.current = os.path.abspath(os.getcwd())
        self.destine = ''

    def _gitInit(self, githubLink):
        print(githubLink)
        os.system('git init')
        os.system('git remote add origin %s' % (githubLink))

    def _isGit(self):
        if ('.git' in os.listdir()):
            return True
        else:
            return False

    def getCurrent(self):
        print(self.current)

    def changePath(self, destine):
        try:
            os.chdir(destine)
            self.destine = destine
            if (self._isGit()):
                print('this directory is git repository')
            else:
                gitProcess = input(
                    'this directory is not git repository, do yo want to git init process? [Y]:Yes [N]:No >> ')
                if (gitProcess == 'Y'):
                    URL = input(
                        'please input your github link to want to init this directory >> ')
                    self._gitInit(URL)
                else:
                    print('Program Off')
        except Exception as e:
            print(e)
            print('destine path ' + destine +
                  ' is not exist in this computer \nplease check your directory path!')

    def getDestine(self):
        print(self.destine)


test = AGMachine()
test.changePath(sys.argv[1])
# test.getDestine()
