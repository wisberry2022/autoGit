import os
import sys
import datetime as dt


class AGMachine:
    def __init__(self):
        self.current = os.path.abspath(os.getcwd())
        self.destine = ''

    def _gitInit(self, githubLink):
        print(githubLink)
        os.system('git init')
        os.system('git remote add origin %s' % (githubLink))
        os.system('git branch -M main')

    def _isGit(self, destine=False):
        if (destine):
            print('isGit exec!', destine)
        else:
            if ('.git' in os.listdir()):
                return True
            else:
                return False

    # 목표 디렉토리 깃 연동 해제
    def _removeGit(self):
        print("\n %s directory's Remove GitRemote Process \n" %
              (self.destine.split('../')[-1]))
        print('============================================== \n')
        gitProcess = input(
            'Do you really want to remove this repository? >>> [Y]:yes [N]:no >> ')
        if (gitProcess == 'Y'):
            os.system('git remote remove origin')
            os.system('rd /s /q .git')
        else:
            print('\n Process End \n')
            print('============================================== \n')

    # 목표 디렉토리 git status 실행
    def _checkStatus(self):
        print("\n %s directory's status \n" % (self.destine.split('../')[-1]))
        print('==============================================')
        os.system('git status')
        print('==============================================')

    # 목표 디렉토리 자동 add / commit / push 메소드
    def _pushToRemote(self):
        date = dt.datetime.now()
        print("\n %s directory's Auto Git Push process START! \n ")
        print("==============================================\n")
        print('Staging Process \n')
        os.system('git add .')
        print("\n==============================================\n")
        print("==============================================\n")
        print('Stage Commit Process \n')
        os.system('git commit -m "auto git upload"')
        print("\n==============================================\n")
        print("==============================================\n")
        print("Remote repo push Process \n")
        os.system('git push origin main')
        print("\n==============================================\n")
        print('Auto Git Push Process END! \n')

    def _menuTemplate(self, *scripts):
        # print(scripts[0])
        print('\n----------------------------------------------')
        print('M E N U    Please input number to want to act')
        print('----------------------------------------------\n')
        for i, v in enumerate(scripts[0]):
            print('%s. %s' % (i, v))
        print('\n----------------------------------------------\n')

    # 목표 디렉토리 이동 및 git status 확인 및 git push
    def _gitAct(self):
        scripts = ["Check your local repo's status",
                   "Push your data in this directory to remote repo (but commit message is auto)", "Remove origin this local repo", "Process End"]
        while (True):
            self._menuTemplate(scripts)
            userInput = input(" >>> ")
            if (userInput == '0'):
                self._checkStatus()
            elif (userInput == '1'):
                self._pushToRemote()
            elif (userInput == '2'):
                self._removeGit()
            elif (userInput == '3'):
                print('\n AutoGit Program End! Thanks! \n')
                print('----------------------------------------------')
                break

    # git repo가 아닌 디렉토리에 접근했을 때 보여주는 메뉴
    def _noGitAct(self):
        scripts = ["Show list of sub directories in this folder", "Process End"]
        while (True):
            self._menuTemplate(scripts)
            userInput = input(" >>> ")
            if (userInput == str(scripts.index("Show list of sub directories in this folder"))):
                print('\n')
                for i, dir in enumerate(os.listdir()):
                    self._isGit(dir)
                    print(i, ' ', dir)
            if (userInput == str(scripts.index("Process End"))):
                print('\n AutoGit Program End! Thanks! \n')
                print('----------------------------------------------')
                break

    def getCurrent(self):
        print(self.current)

    def getDestine(self):
        print(self.destine)

    # 목표 디렉토리 이동 및 깃 연동
    def startAutoGit(self, destine):
        try:
            os.chdir(destine)
            self.destine = destine
            if (self._isGit()):
                print('this directory is git repository')
                self._gitAct()
            else:
                gitProcess = input(
                    'this directory is not git repository, do yo want to git init process? [Y]:Yes [N]:No >> ')
                if (gitProcess == 'Y'):
                    URL = input(
                        'please input your github link to want to init this directory >> ')
                    self._gitInit(URL)
                else:
                    # print('Program Off')
                    self._noGitAct()
        except Exception as e:
            print(e)
            print('destine path ' + destine +
                  ' is not exist in this computer \nplease check your directory path!')


test = AGMachine()
test.startAutoGit(sys.argv[1])
