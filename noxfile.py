import nox

@nox.session(python=['2.7', '3.4','3.5', '3.6', '3.7', 'pypy'])
def unit(session):
    session.env['PYTHONWARNINGS'] = 'always::DeprecationWarning'
    session.install('-r', 'dev-requirements.txt')
    session.install('.[secure,socks]')
    session.run('pip', '--version')
    session.run('python', '--version')
    session.run('python', '-c', 'import struct; print(struct.calcsize(\'P\') * 8)')
    session.run('coverage', 'run', '--parallel-mode', '-m', 'pytest', '-r', 'sx', 'test')
    session.run('coverage', 'combine')
    session.run('coverage', 'report', '-m')

@nox.session(python='2.7')
def docs(session):
    session.env['PYTHONWARNINGS'] = 'always::DeprecationWarning'
    session.install('-r/usr/local/google/home/crwilcox/workspace/urllib3/docs/requirements.txt')
    session.install('.')
    session.run('rm', '-rf', '/usr/local/google/home/crwilcox/workspace/urllib3/docs/_build')
    session.run('make', '-C', '/usr/local/google/home/crwilcox/workspace/urllib3/docs', 'html')

@nox.session(python='3.4')
def flake8py3(session):
    session.env['PYTHONWARNINGS'] = 'always::DeprecationWarning'
    session.install('flake8')
    session.install('.')
    session.run('flake8', '--version')
    session.run('flake8', 'setup.py', 'docs', 'dummyserver', 'urllib3', 'test')

@nox.session(python='2.7')
def gae(session):
    session.env['GAE_SDK_PATH'] = ''
    session.env['PYTHONWARNINGS'] = 'always::DeprecationWarning'
    session.install('-r/usr/local/google/home/crwilcox/workspace/urllib3/dev-requirements.txt')
    session.install('.')
    session.run('py.test', '-r', 'sx', 'test/appengine')
