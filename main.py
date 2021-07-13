import subprocess

if __name__ == '__main__':
    ps = subprocess.Popen(('find', '/etc', '-name', '*.config'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = subprocess.check_output(('wc', '-l'), stdin=ps.stdout)
    # ps.wait()
    print(output.decode('utf-8'))


